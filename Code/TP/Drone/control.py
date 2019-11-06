#!/usr/bin/env python
# coding: utf-8
import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
from std_msgs.msg import UInt8, Empty
from std_srvs.srv import Trigger, TriggerResponse

# Publishers:
pub_start, pub_pause, pub_cmd, pub_flip, pub_reset = 0, 0, 0, 0, 0

# Etat précédent du bouton:
btn_1_prev = False

# Mode: "loisir" ou "surveillance"
mode = "loisir"


## Subscriber handle ##

# Traitement du joystick pour contrôler le drone:
def joystick_handle(data):
    global btn_1_prev, mode

    ## Récupère les données du joystick ##

    # Axes:
    axe_gx, axe_gy = data.axes[0], data.axes[1]
    axe_dx, axe_dy = data.axes[3], data.axes[4]

    # Buttons:
    btn_pause, btn_start = data.buttons[8] == 1,  data.buttons[9] == 1
    btn_1, btn_2   = data.buttons[0] == 1, data.buttons[1] == 1
    btn_g1, btn_g2 = data.buttons[4] == 1, data.buttons[6] == 1
    btn_r1, btn_r2 = data.buttons[5] == 1, data.buttons[7] == 1

    # Si le bouton vient d'être appuyé:
    if btn_1 != btn_1_prev and btn_1 == True:
        # Modifie le mode: 
        mode = "surveillance" if mode == "loisir" else "loisir"
        rospy.loginfo("Modification du mode en: %s", mode)
    btn_1_prev = btn_1  # Sauvegarde l'état précédent du bouton
    
    # Logs:
    rospy.loginfo("x: %.2f %.2f, y: %.2f %.2f", axe_gx, axe_gy, axe_dx, axe_dy)
    rospy.loginfo("pause: %s, start: %s, 1: %s, 2: %s", btn_pause, btn_start, btn_1, btn_2)
    rospy.loginfo("g1: %s, g2: %s, r1: %s, r2: %s\n", btn_g1, btn_g2, btn_r1, btn_r2)

    ## Actions envoyées au drone ##
    
    # Pause / Start / Reset:
    if btn_pause: pub_pause.publish()
    if btn_start: pub_start.publish()
    if btn_2: pub_reset.publish()

    # Quitte la fonction si ce n'est pas le mode "loisir":
    # (pour ne pas réaliser de déplacement)
    if mode != "loisir": return

    # Déplacement:
    cmd = Twist()    
    cmd.linear.x = axe_gy
    cmd.linear.y = axe_gx
    cmd.linear.z = axe_dy
    cmd.angular.z = axe_dx 
    pub_cmd.publish(cmd)   
    
    # Flip:
    if btn_g1: pub_flip.publish(0)  # Flip Forward
    if btn_g2: pub_flip.publish(1)  # Flip Backward
    if btn_r1: pub_flip.publish(2)  # Flip Right
    if btn_r2: pub_flip.publish(3)  # Flip Left


## Services ##

# Défini le mode en "loisir":
def setModeLoisir(req):
    global mode
    ok = False
    if mode == "surveillance" :
        mode = "loisir"
        ok = True   
    return TriggerResponse(ok, "")

# Définit le mode en "surveillance":
def setSurveillance(req):
    global mode
    ok = False
    if mode == "loisir" :
        mode = "surveillance"
        ok = True
    return TriggerResponse(ok, "")


# Initialisation du noeud:
def init():
    global pub_start, pub_pause, pub_cmd, pub_flip, pub_reset
    
    # Init node:
    rospy.init_node('SubscriberControl', anonymous=True)

    # Subscriber:
    rospy.Subscriber("/joy", Joy, joystick_handle)

    # Publishers:
    pub_start = rospy.Publisher("/bebop/takeoff", Empty, queue_size=10)
    pub_pause = rospy.Publisher("/bebop/land",    Empty, queue_size=10)
    pub_cmd   = rospy.Publisher("/bebop/cmd_vel", Twist, queue_size=10)
    pub_flip  = rospy.Publisher("/bebop/flip",    UInt8, queue_size=10)
    pub_reset = rospy.Publisher("/bebop/reset",   Empty, queue_size=10)

    # Services:
    s1 = rospy.Service('modeSurveillance', Trigger, setSurveillance)
    s2 = rospy.Service('modeLoisir', Trigger, setModeLoisir)


if __name__ == '__main__':
    # Initialiation du noeud:
    init()

    # Pour le mode "surveillance": envoi une rotation constante
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        if mode == "surveillance":
            cmd = Twist()    
            cmd.angular.z = 0.5 
            pub_cmd.publish(cmd)     
        rate.sleep()
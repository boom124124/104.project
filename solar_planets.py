import cv2

img = cv2.imread('solar-system.jpg')
cv2.imshow('output',img)
cv2.putText(img,"Sun",(240,124),cv2.FONT_HERSHEY_COMPLEX,2.4,(40,80,255))
cv2.putText(img,"Mercury",(120,250), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Venus",(200,280), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Earth",(280,240), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Moon",(300,124), cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0))
cv2.putText(img,"Mars",(370,270), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Jupiter",(560,370), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Saturn",(800,300), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Uranus",(980,300), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Neptune",(1100,300), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.imshow('output',img)
cv2.waitKey(0)


import os
import cv2
import mediapipe as mp
import numpy as np
from all_reference_poses_point_deletable import reference_pose


image_drawed = "Drawed reference image deletable"
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)


# for filename in os.listdir(image_drawed):
#     if filename.endswith(".jpg") or filename.endswith(".png"):  # Adjust the file extensions as needed
#         # this will return a tuple of root and extension
#         print(filename)
#         image_path = os.path.join(image_drawed, filename)
#         image = cv2.imread(image_path)
#         height, width, _ = image.shape

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            continue
            
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(rgb_frame)

        if results.pose_landmarks:
            pose_landmarks = [(lm.x, lm.y) for lm in results.pose_landmarks.landmark]

            mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                                mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                                mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                                )

        cv2.imshow("Pose Estimation", frame)
                
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()
        
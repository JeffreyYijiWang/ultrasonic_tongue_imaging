import spoutpy
import cv2

receiver = spoutpy.SpoutReceiver()
receiver.create_receiver("OBS_Spout_jeffrey")  # Matches your Spout output name

while True:
    frame = receiver.receive()
    if frame is not None:
        frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR)
        cv2.imshow("Spout Feed", frame_bgr)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

receiver.release()
cv2.destroyAllWindows()
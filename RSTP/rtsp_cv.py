import cv2
import time

def display_rtsp_stream(rtsp_url):
    """
    Displays an RTSP stream using OpenCV with "Hello" text.

    Args:
        rtsp_url (str): The RTSP URL of the stream.
    """
    fps=0
    try:
        cap = cv2.VideoCapture(rtsp_url)

        if not cap.isOpened():
            print(f"Error: Could not open RTSP stream from {rtsp_url}")
            return

        while True:
            tStart=time.time()
            ret, frame = cap.read()

            if not ret:
                print("Error: Could not read frame from stream. Reconnecting...")
                cap.release()
                cap = cv2.VideoCapture(rtsp_url)  # Attempt to reconnect
                if not cap.isOpened():
                    print("Error: Reconnection failed. Exiting.")
                    break
                continue

            # Add "Hello" text to the frame
            cv2.putText(frame, str(int(fps)), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

            cv2.imshow("RTSP Stream", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
            tEnd=time.time()
            loopTime=tEnd-tStart
            fps=.9*fps + .1*(1/loopTime)

        cap.release()
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    rtsp_url = "rtsp://192.168.12.240:8554/stream1"  # Replace with your RTSP URL
    display_rtsp_stream(rtsp_url)

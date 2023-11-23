import tkinter as tk
from PIL import ImageGrab

class ScreenCapture:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-alpha', 0.2)  # 투명도 설정
        self.root.attributes("-topmost", True)  # 항상 위에 표시

        self.start_x = self.start_y = self.end_x = self.end_y = 0

        self.rect_id = None
        self.canvas = tk.Canvas(self.root, bg="black", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=tk.YES)

        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y

        if self.rect_id:
            self.canvas.delete(self.rect_id)

        self.rect_id = self.canvas.create_rectangle(self.start_x, self.start_y, 1, 1, outline='red', width=7)

    def on_mouse_drag(self, event):
        self.end_x = event.x
        self.end_y = event.y

        self.canvas.coords(self.rect_id, self.start_x, self.start_y + 60, self.end_x, self.end_y + 60)

    def on_button_release(self, event):
        # 캡쳐 로직을 이곳에 추가하면 됩니다.
        capture_x0 = min(self.start_x, self.end_x)
        capture_y0 = min(self.start_y, self.end_y)
        capture_x1 = max(self.start_x, self.end_x)
        capture_y1 = max(self.start_y, self.end_y)

        captured_area = (capture_x0, capture_y0 + 55, capture_x1, capture_y1 + 55)
        print("캡쳐된 영역:", captured_area)
        root.destroy()
        im = ImageGrab.grab(bbox=captured_area)
        file_name = "captured_image.png"  # 저장할 파일 이름
        im.save(file_name)  # 이미지 저장
        print(f"캡쳐된 이미지를 '{file_name}'로 저장했습니다.")
        # 여기서 캡쳐된 영역을 사용하여 필요한 작업을 수행할 수 있습니다.

if __name__ == "__main__":
    root = tk.Tk()
    root.attributes("-fullscreen", True)  # 전체 화면으로 설정
    root.configure(bg='black')  # 검은색 배경 설정

    capture_app = ScreenCapture(root)
    root.mainloop()

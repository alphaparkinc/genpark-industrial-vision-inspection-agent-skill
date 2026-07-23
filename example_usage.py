from client import IndustrialVisionInspectionAgentClient

def main():
    client = IndustrialVisionInspectionAgentClient()
    res = client.inspect_frame(image_frame_url="https://factory.example.com/cam_01/frame_1092.jpg")
    print(f"Pass Inspection: {res['pass_inspection']}")
    print(f"Defects Found: {len(res['defects_detected'])}")

if __name__ == "__main__":
    main()

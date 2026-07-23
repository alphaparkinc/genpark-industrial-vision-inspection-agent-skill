class IndustrialVisionInspectionAgentClient:
    def inspect_frame(self, image_frame_url: str, defect_threshold: float = 0.85) -> dict:
        defects = []
        # Mock inspection logic
        return {
            "defects_detected": defects,
            "pass_inspection": len(defects) == 0
        }

from htr.htr_engine import HTREngine


if __name__ == "__main__":
    engine = HTREngine()
    engine.load_inferencer('./RmtDet')
    engine.run_inference("RmtDetRegion_region", "")

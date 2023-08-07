from htr_pipeline.htr_engine import HTREngine


if __name__ == "__main__":
    engine = HTREngine()
    engine.load_inferencer('/workspaces/htr_pipeline/notebooks/RmtDet')
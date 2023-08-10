from htr.htr_engine import HTREngine

if __name__ == "__main__":
    engine = HTREngine()
    engine.load_inferencer("test", "./RmtDet")
    engine.load_inferencer("test1", "./RmtDet")

    print(engine.inferencer_keys)

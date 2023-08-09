from htr.htr_engine import HTREngine

if __name__ == "__main__":
    engine = HTREngine()
    engine.load_inferencer("test",'./RmtDet')
    print(engine.inferencer_keys['test'].predict("test") )

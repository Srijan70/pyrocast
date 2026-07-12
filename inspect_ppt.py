from pptx import Presentation

def inspect_presentation(filepath):
    prs = Presentation(filepath)
    for i, slide in enumerate(prs.slides):
        print(f"\n--- Slide {i+1} ---")
        for j, shape in enumerate(slide.shapes):
            print(f"Shape {j} ({shape.shape_type}): Name={shape.name}")

if __name__ == "__main__":
    inspect_presentation("PyroCast-Final-Presentation.pptx")

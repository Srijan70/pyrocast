from pptx import Presentation
import sys

def replace_image_in_slide(filepath, output_path, image_path):
    prs = Presentation(filepath)
    
    slide = prs.slides[7]
    pic_shape = None
    
    for shape in slide.shapes:
        if shape.shape_type == 13:  # msoPicture
            pic_shape = shape
            break
            
    if not pic_shape:
        print("Could not find picture in Slide 8.")
        sys.exit(1)
        
    left = pic_shape.left
    top = pic_shape.top
    width = pic_shape.width
    height = pic_shape.height
    
    element = pic_shape.element
    element.getparent().remove(element)
    
    slide.shapes.add_picture(image_path, left, top, width, height)
    
    prs.save(output_path)
    print("Replaced image and saved to", output_path)

if __name__ == "__main__":
    replace_image_in_slide("PyroCast-Final-Presentation.pptx", "PyroCast-Final-Presentation.pptx", "current_output.png")

import json

printEnabled = True

def custom_print(*args, **kwargs):
    if printEnabled:
        print(*args, **kwargs)

def load_name_mapping(filename):
    with open(filename, "r") as file:
        return json.load(file)

def update_name_mapping(new_names_mapping, name_mapping_json_path):
    name_mapping = load_name_mapping(name_mapping_json_path)
    name_mapping.update(new_names_mapping)
    save_name_mapping(name_mapping, name_mapping_json_path)
    print("Updated name mapping has been saved.")

def save_name_mapping(mapping, path):
    with open(path, "w") as file:
        json.dump(mapping, file, indent=4)

def scale_glyph(glyph):
    target_width = 1024
    target_height = 1024
    bbox = glyph.boundingBox()
    glyph_width = bbox[2] - bbox[0]
    glyph_height = bbox[3] - bbox[1]

    # Calculate scaling factors
    scale_x = target_width / glyph_width if glyph_width != 0 else 1
    scale_y = target_height / glyph_height if glyph_height != 0 else 1
    scale_factor = min(scale_x, scale_y) * 0.87

    # Apply scaling to fit within the target bounding box
    glyph.transform((scale_factor, 0, 0, scale_factor, 0, 0))

    # Get the new bounding box after scaling
    bbox = glyph.boundingBox()
    glyph_width = bbox[2] - bbox[0]
    glyph_height = bbox[3] - bbox[1]

    # Calculate the translation needed to center the glyph
    left_offset = (target_width - glyph_width) / 2
    top_offset = (target_height - glyph_height) / 2
    translate_x = -bbox[0] + left_offset
    translate_y = -bbox[1] + top_offset

    # Apply the translation to center the glyph
    glyph.transform((1, 0, 0, 1, translate_x, translate_y))

    # Set the glyph width and vertical width to the target size
    glyph.width = target_width
    glyph.vwidth = target_height

def createCardHtml(name, code_point, add_class):
    code_point_str = str(code_point)  # Ensure code_point is a string
    return f"""
    <div class="card-client">
        <div class="icon_main">
            <i class="{add_class}_{name} copy_class_js ico_size-sm"></i>
        </div>
        <p class="name-client"> {name}
            <span>#{code_point_str }</span>
        </p>

        <div class="icon_demo_row_cont">
            <div class="icon_demo_row">
                <i class="{add_class}_{name} copy_class_js ico_size-sm"></i>
                <i class="{add_class}_{name} copy_class_js ico_size-md"></i>
                <i class="{add_class}_{name} copy_class_js ico_size-lg"></i>
                <i class="{add_class}_{name} copy_class_js ico_size-xl"></i>
            </div>
        </div>

        <div class="btn_demo_row">
            <button class='btn_demo copy_class_btn_js'>copy class</button>
        </div>
    </div>
    """

def transform_name(name):
    # Make the entire name lowercase
    name = name.lower()
    # Replace spaces with underscores
    transformed_name = name.replace(" ", "_")
    return transformed_name

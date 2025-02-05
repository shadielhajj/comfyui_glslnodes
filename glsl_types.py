class GlslInt:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("INT", { "default": 0.0 }),
            }
        }
    
    CATEGORY = "GLSL"
    FUNCTION = "main"
    # DESCRIPTION = """
    # This node returns an integer value.
    # """

    RETURN_TYPES = ("INT", )
    RETURN_NAMES = ("int", )

    def main(self, value):
        return (value, )
    

class GlslFloat:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("FLOAT", { "default": 0.0, "min": -0xffffffffffffffff, "max": 0xffffffffffffffff, "step": 0.001 }),
            }
        }
    
    CATEGORY = "GLSL"
    FUNCTION = "main"
    # DESCRIPTION = """
    # This node returns a float value.
    # """

    RETURN_TYPES = ("FLOAT", )
    RETURN_NAMES = ("float", )

    def main(self, value):
        return (value, )
    

class GlslVec2:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "x": ("FLOAT", { "default": 0.0, "min": -0xffffffffffffffff, "max": 0xffffffffffffffff, "step": 0.001 }),
                "y": ("FLOAT", { "default": 0.0, "min": -0xffffffffffffffff, "max": 0xffffffffffffffff, "step": 0.001 }),
            }
        }
    
    CATEGORY = "GLSL"
    FUNCTION = "main"
    # DESCRIPTION = """
    # This node returns a vec2 value.
    # """

    RETURN_TYPES = ("VEC2", )
    RETURN_NAMES = ("vec2", )

    def main(self, x, y):
        return ((x, y), )
    

class GlslVec2Pos:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "pos": ("VEC2POS", { "default": (0.0, 0.0), }),
            }
        }
    
    CATEGORY = "GLSL"
    FUNCTION = "main"
    # DESCRIPTION = """
    # This node returns a vec2 value from a 2D position.
    # """

    RETURN_TYPES = ("VEC2", )
    RETURN_NAMES = ("vec2", )

    def main(self, pos):
        pos = pos.split(",")
        return ((float(pos[0]), float(pos[1])), )


class GlslVec3:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "x": ("FLOAT", { "default": 0.0, "min": -0xffffffffffffffff, "max": 0xffffffffffffffff, "step": 0.001 }),
                "y": ("FLOAT", { "default": 0.0, "min": -0xffffffffffffffff, "max": 0xffffffffffffffff, "step": 0.001 }),
                "z": ("FLOAT", { "default": 0.0, "min": -0xffffffffffffffff, "max": 0xffffffffffffffff, "step": 0.001 }),
            }
        }
    
    CATEGORY = "GLSL"
    FUNCTION = "main"
    # DESCRIPTION = """
    # This node returns a vec3 value.
    # """

    RETURN_TYPES = ("VEC3", )
    RETURN_NAMES = ("vec3", )

    def main(self, x, y, z):
        return ((x, y, z), )
    

class GlslVec3Pos:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "pos": ("VEC3POS", { "default": (0.0, 0.0, 0.0),}),
            }
        }
    
    CATEGORY = "GLSL"
    FUNCTION = "main"
    # DESCRIPTION = """
    # This node returns a vec3 value. From a 3D position.
    # """

    RETURN_TYPES = ("VEC3", )
    RETURN_NAMES = ("vec3", )

    def main(self, pos):
        pos = pos.split(",")
        return ((float(pos[0]), float(pos[1]), float(pos[1])), )


class GlslVec4:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "x": ("FLOAT", { "default": 0.0, "min": -0xffffffffffffffff, "max": 0xffffffffffffffff, "step": 0.001 }),
                "y": ("FLOAT", { "default": 0.0, "min": -0xffffffffffffffff, "max": 0xffffffffffffffff, "step": 0.001 }),
                "z": ("FLOAT", { "default": 0.0, "min": -0xffffffffffffffff, "max": 0xffffffffffffffff, "step": 0.001 }),
                "w": ("FLOAT", { "default": 0.0, "min": -0xffffffffffffffff, "max": 0xffffffffffffffff, "step": 0.001 }),
            }
        }
    
    CATEGORY = "GLSL"
    FUNCTION = "main"
    # DESCRIPTION = """
    # This node returns a vec4 value.
    # """

    RETURN_TYPES = ("VEC4", )
    RETURN_NAMES = ("vec3", )

    def main(self, x, y, z, w):
        return ((x, y, z,w), )
    

class GlslVec4Color:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "color": ("VEC4COLOR", { "default": (1.0, 0.0, 0.0, 1.0) }),
            }
        }
    
    CATEGORY = "GLSL"
    FUNCTION = "main"
    # DESCRIPTION = """
    # This node returns a vec4 value from a color.
    # """

    RETURN_TYPES = ("VEC4", )
    RETURN_NAMES = ("vec4", )

    def main(self, color):
        color = color.split(",")
        return ((float(color[0]), float(color[1]), float(color[2]), float(color[3]) ), )
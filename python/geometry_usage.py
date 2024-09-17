import geometry

current_test = "none"

def test_begin(type):
    current_test = type
    print("tests/{} [begin]: test started".format(current_test))

def test_values(value, value2):
    print("tests/{} [value set]: value {} set to {}".format(current_test, value, value2))

def test_results(result):
    print("tests/{} [result]: {}".format(current_test, result))

test_begin("circle")

ncircle = geometry.circle(5)

test_values("radius", "5")

ncircle_radius = ncircle.radius
ncircle_diameter = ncircle.diameter
ncircle_pi_fn = ncircle.pi()
ncircle_pi_var = ncircle.pie

test_results("radius:   {}".format(ncircle_radius))
test_results("diameter: {}".format(ncircle_diameter))
test_results("pi fn:    {}".format(ncircle_pi_fn))
test_results("pi var:   {}".format(ncircle_pi_var))

test_begin("rectangle")

nsquare = geometry.rectangle(5, 5)

test_values("width", "5")
test_values("height", "5")

nsquare_width = nsquare.width
nsquare_height = nsquare.height
nsquare_area = nsquare.area()

test_results("width:  {}".format(nsquare_width))
test_results("height: {}".format(nsquare_height))
test_results("area:   {}".format(nsquare_area))

test_begin("triangle")

ntriangle = geometry.triangle(5, 5)

test_values("width", "5")
test_values("height", "5")

ntriangle_width = ntriangle.width
ntriangle_height = ntriangle.height
ntriangle_area = ntriangle.area()

test_results("width:  {}".format(ntriangle_width))
test_results("height: {}".format(ntriangle_height))
test_results("area:   {}".format(ntriangle_area))

print("tests done")
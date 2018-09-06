class Sphere(object):
	slices = 40
	stacks = 40

	def __init__(self, radius, position, color):
		self.radius = radius
		self.position = position
		self.color = color
		self.quadratic = gluNewQuadric()

	def render(self):
		glPushMatrix()
		glTranslatef(*self.position)
		glMaterialfv(GL_FRONT, GL_DIFFUSE  , self.color)
		glMaterialfv(GL_FRONT, GL_AMBIENT  , (0.0, 0.0, 0.0, 1.0))
        glMaterialfv(GL_FRONT, GL_DIFFUSE  , (0.1, 0.5, 0.8, 1.0))
        glMaterialfv(GL_FRONT, GL_SPECULAR , (0.0, 0.0, 0.0, 1.0))
        glMaterialfv(GL_FRONT, GL_SHININESS, 0.0)
        glMaterialfv(GL_FRONT, GL_EMISSION , (0.0, 0.0, 0.0, 1.0))
		gluSphere(self.quadratic, self.radius,
				  Sphere.slices, Sphere.stacks)
		glPopMatrix()
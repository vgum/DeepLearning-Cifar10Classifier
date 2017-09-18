import Cifar10Classifier 
import Original

# Differant augmentation represents
singles = [[1],[2],[3],[4],[5]]
doubles = [[1, 2],[1, 3],[1, 4],[1, 5],[2, 3],[2, 4],[2, 5],[3, 4],[3, 5],[4, 5]]
triplets = [[1, 2, 3],[1, 2, 4],[1, 2, 5],[1, 3, 4],[1, 3, 5],[1, 4, 5],[2, 3, 4],[2, 3, 5],[2, 4, 5],[3, 4, 5]] 
quadruples = [[1, 2, 3, 4],[1, 2, 3, 5],[1, 2, 4, 5],[1, 3, 4, 5],[2, 3, 4, 5]]
fives = [[1,2,3,4,5]]

for group in singles:
	Cifar10Classifier.setupandrun(group)
for group in doubles:
	Cifar10Classifier.setupandrun(group)
for group in triplets:
	Cifar10Classifier.setupandrun(group)
for group in quadruples:
	Cifar10Classifier.setupandrun(group)
for group in fives:
	Cifar10Classifier.setupandrun(group)

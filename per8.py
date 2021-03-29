from ai_pkg.planning import PlanningProblem, Action, goal_test
from ai_pkg.utils import expr
#doubleadalah salah satu contoh kasus sederhana tentang multiagen
def double_tennis_problem():
	#apabila pada kondisi awal posisi pemain A berada dikiribelakang dan pemain B berada pada
	#posisi kanan depan, bola dipukul oleh lawan menuju kanan belakang
	initial = 'At(A, LeftBaseLine) & At(B, RightNet) & Approaching(Ball,RightBaseLine) & Team(A, B) & Team(B, A)'
	goal = 'Returned(Ball) & At(a, RightNet) & At(a, LeftNet)'
	#Returned(Ball): salah satu pemain berhasil memukul dan mengembalikan bola 
	#dari posisi yang benar yang menyebabkan bola kembali ke daerah tim lawan.
	action = [Action('Hit(player, Ball, loc)',precond='Approaching(Ball, loc) & At(player, loc)',effect='Returned(Ball)'),
	#Approaching(Ball, loc):Bola Balldioper menuju posisi loc
	#At(Player, loc): Pemain player berada pada posisi loc
	#Hit(player, ball, loc) : Aksi mengembalikan Bola Ball jika ada pemain player yang berada di posisi loc
	Action('Go(player, to, loc)',precond='At(player, loc)',effect='At(player, to)')]
	#Go(player, to, loc) : pemain player bergerak dari posisi lock ke posisi to
	return PlanningProblem(init=initial,goals=goal,actions=action)

if __name__=="__main__":
	p = double_tennis_problem()
	print(goal_test(p.goals, p.init))
	solution = [expr('Go(A, RightBaseLine, LeftBaseLine)'),expr('Hit(A, Ball, RightBaseLine)')]
	for action in solution:
		p.act(action)

	print(goal_test(p.goals, p.init))
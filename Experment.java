
public class Experment {
	static int count = 1;

	public static List<TreeNode> method(List<TreeNode> treeNodes) {
		List<TreeNode> trees = new ArrayList<MainMenu>();
		for (TreeNode treeNode : treeNodes) {
			if (treeNode.getUrl != null && treeNode.getId().length == 3) {
				trees.add(treeNode);
			} else {
				for (TreeNode it : treeNodes) {
					if (it.getUrl != null && it.getId().length - 3 == treeNode.getId()) {
						treeNode.getChildren().add(it);
					}
					if (it.getId().length = treeNode.getId().length && it.getUrl != null) {
						trees.add(it);
					} else {
						break;
					}
					count = count + 3;
				}
			}
		}
		
	}
}
//���ݱ��ʽ
//"001"	"һ���˵�1"		""
//"001001"	"�����˵�1-1"		""
//"001001001"	"�����˵�1-1-1"		"url1"
//"001001002"	"�����˵�1-1-2"		"url1"
//"001002"	"�����˵�1-2"		""
//"001002001"	"�����˵�1-2-1"		"url1"
//"001003"	"�����˵�1-3"		"url1"

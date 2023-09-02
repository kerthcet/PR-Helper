import unittest

from utils.util import parse_content


class TestUtil(unittest.TestCase):
    def test_parse_content(self):
        content = "<!--  Thanks for sending a pull request!  Here are some tips for you:\r\n\r\n1. If this is your first time, please read our contributor guidelines: https://git.k8s.io/community/contributors/guide/first-contribution.md#your-first-contribution and developer guide https://git.k8s.io/community/contributors/devel/development.md#development-guide\r\n2. Please label this pull request according to what type of issue you are addressing, especially if this is a release targeted pull request. For reference on required PR/issue labels, read here:\r\nhttps://git.k8s.io/community/contributors/devel/sig-release/release.md#issuepr-kind-label\r\n3. Ensure you have added or ran the appropriate tests for your PR: https://git.k8s.io/community/contributors/devel/sig-testing/testing.md\r\n4. If you want *faster* PR reviews, read how: https://git.k8s.io/community/contributors/guide/pull-requests.md#best-practices-for-faster-reviews\r\n5. If the PR is unfinished, see how to mark it: https://git.k8s.io/community/contributors/guide/pull-requests.md#marking-unfinished-pull-requests\r\n-->\r\n\r\n#### What type of PR is this?"
        generated_content = "\n#### What type of PR is this?\n"
        self.assertEqual(parse_content(content=content), generated_content)

        content = "<!--  Thanks for sending a pull request! -->My pleasure"
        generated_content = "My pleasure\n"
        self.assertEqual(parse_content(content=content), generated_content)

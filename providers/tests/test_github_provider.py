import unittest

from providers.github_provider import (
    convert_to_diff_url,
    convert_to_pull_pr_url,
    convert_to_pull_commit_url,
    split_line_break,
)


class TestGithubUtil(unittest.TestCase):
    def test_convert_to_diff_url(self):
        former_url = "https://github.com/kubernetes/kubernetes/pull/120252"
        target_url = "https://patch-diff.githubusercontent.com/raw/kubernetes/kubernetes/pull/120252.diff"
        self.assertEqual(convert_to_diff_url(url=former_url), target_url)

    def test_convert_to_pull_pr_url(self):
        former_url = "https://github.com/kubernetes/kubernetes/pull/120252"
        target_url = "https://api.github.com/repos/kubernetes/kubernetes/pulls/120252"
        self.assertEqual(convert_to_pull_pr_url(former_url), target_url)

    def test_convert_to_pull_commit_url(self):
        former_url = "https://github.com/kubernetes/kubernetes/pull/120252"
        target_url = (
            "https://api.github.com/repos/kubernetes/kubernetes/pulls/120252/commits"
        )
        self.assertEqual(convert_to_pull_commit_url(former_url), target_url)

    def test_split_line_break(self):
        former_content = "Rename listers.go to faker_listers.go\n\nSigned-off-by: kerthcet <kerthcet@gmail.com>"
        target_content = "Rename listers.go to faker_listers.go"
        self.assertEqual(split_line_break(former_content), target_content)
        self.assertEqual(split_line_break(target_content), target_content)

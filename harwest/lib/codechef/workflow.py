from harwest.lib.abstractworkflow import AbstractWorkflow
from harwest.lib.codechef.client import CodechefClient


class CodechefWorkflow(AbstractWorkflow):
  def __init__(self, user_data):
    super().__init__(CodechefClient(user_data['codechef']), user_data)

  def enrich_submission(self, submission):
    problem_name = self.client.get_problem_name(submission['problem_url'])
    # For CodeChef, contest_id serves as the problem index
    submission['problem_index'] = submission['contest_id']
    submission['problem_name'] = problem_name

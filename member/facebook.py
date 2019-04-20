from .models import Member, PaymentMethod


def create_member(strategy, details, response, user=None, *args, **kwargs):
	if user and kwargs['is_new']:
		member = Member.create(user=user, nickname='Player{}'.format(user.id))
		PaymentMethod.create(account_number=user.id, member=member)
		
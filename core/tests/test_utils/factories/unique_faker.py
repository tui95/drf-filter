import factory


class UniqueFaker(factory.Faker):
    """
    Make the generated values to be unique

    Notes:
        taken from https://github.com/FactoryBoy/factory_boy/pull/820#issuecomment-1004802669
    """

    @classmethod
    def _get_faker(cls, locale=None):
        return super()._get_faker(locale=locale).unique

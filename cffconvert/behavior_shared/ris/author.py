from abc import abstractmethod


class RisAuthorShared:

    def __init__(self, author_cff):
        self._author_cff = author_cff
        self._behaviors = {
            'GFAN': self._from_given_and_last,
            'GFA.': self._from_given_and_last,
            'GF.N': self._from_given_and_last,
            'GF..': self._from_given_and_last,
            'G.AN': self._from_name,
            'G.A.': self._from_alias,
            'G..N': self._from_name,
            'G...': self._from_given,
            '.FAN': self._from_last,
            '.FA.': self._from_last,
            '.F.N': self._from_last,
            '.F..': self._from_last,
            '..AN': self._from_name,
            '..A.': self._from_alias,
            '...N': self._from_name,
            '....': RisAuthorShared._from_thin_air
        }

    def _exists_nonempty(self, key):
        value = self._author_cff.get(key, None)
        return value is not None and value != ''

    def _from_alias(self):
        return 'AU  - ' + self._author_cff.get('alias') + '\n'

    def _from_given_and_last(self):
        return 'AU  - ' + self._get_full_last_name() + ', ' + self._author_cff.get('given-names') + '\n'

    def _from_given(self):
        return 'AU  - ' + self._author_cff.get('given-names') + '\n'

    def _from_last(self):
        return 'AU  - ' + self._get_full_last_name() + '\n'

    def _from_name(self):
        return 'AU  - ' + self._author_cff.get('name') + '\n'

    @staticmethod
    def _from_thin_air():
        return None

    def _get_full_last_name(self):
        nameparts = [
            self._author_cff.get('name-particle'),
            self._author_cff.get('family-names'),
            self._author_cff.get('name-suffix')
        ]
        return ' '.join([n for n in nameparts if n is not None])

    @abstractmethod
    def as_string(self):
        pass


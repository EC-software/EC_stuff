class FeatureProcessor(object):

    def __init__(self):
        self.features = []
        self.distinct_etage = set()
        self.group_id = None

    def flush(self):
        max_etage = max(self.distinct_etage)
        min_etage = min(self.distinct_etage)
        n_over_ground = len([x for x in self.distinct_etage if x > -1])
        n_distinct = len(self.distinct_etage)
        etages = sorted(list(self.distinct_etage))
        for feature in self.features:
            etage = int(feature.getAttribute('dar_etage'))
            feature.setAttribute('dar_etage_max', max_etage)
            feature.setAttribute('dar_etage_min', min_etage)
            feature.setAttribute('dar_etage_n_distinct', n_distinct)
            feature.setAttribute('dar_etage_n_over_ground', n_over_ground)
            feature.setAttribute('dar_etage_nbr', etages.index(etage))
            self.pyoutput(feature)
        self.features = []
        self.group_id = None
        self.distinct_etage = set()

    def input(self,feature):
        group_id = feature.getAttribute('dar_adgangsadresseid')
        if self.group_id is None:
            self.group_id = group_id
        elif self.group_id != group_id:
            self.flush()
            self.group_id = group_id
        etage = int(feature.getAttribute('dar_etage'))
        self.distinct_etage.add(etage)
        self.features.append(feature)

    def close(self):
        self.flush()

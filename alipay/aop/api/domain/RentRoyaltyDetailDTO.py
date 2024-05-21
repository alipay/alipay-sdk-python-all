#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RoyaltyDTO import RoyaltyDTO


class RentRoyaltyDetailDTO(object):

    def __init__(self):
        self._royalties = None
        self._stage_no = None

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if isinstance(value, list):
            self._royalties = list()
            for i in value:
                if isinstance(i, RoyaltyDTO):
                    self._royalties.append(i)
                else:
                    self._royalties.append(RoyaltyDTO.from_alipay_dict(i))
    @property
    def stage_no(self):
        return self._stage_no

    @stage_no.setter
    def stage_no(self, value):
        self._stage_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.royalties:
            if isinstance(self.royalties, list):
                for i in range(0, len(self.royalties)):
                    element = self.royalties[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.royalties[i] = element.to_alipay_dict()
            if hasattr(self.royalties, 'to_alipay_dict'):
                params['royalties'] = self.royalties.to_alipay_dict()
            else:
                params['royalties'] = self.royalties
        if self.stage_no:
            if hasattr(self.stage_no, 'to_alipay_dict'):
                params['stage_no'] = self.stage_no.to_alipay_dict()
            else:
                params['stage_no'] = self.stage_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentRoyaltyDetailDTO()
        if 'royalties' in d:
            o.royalties = d['royalties']
        if 'stage_no' in d:
            o.stage_no = d['stage_no']
        return o



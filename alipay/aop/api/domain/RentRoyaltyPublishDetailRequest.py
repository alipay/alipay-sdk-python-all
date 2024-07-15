#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RoyaltyInfoRequest import RoyaltyInfoRequest


class RentRoyaltyPublishDetailRequest(object):

    def __init__(self):
        self._royalty_info = None
        self._stage_no = None

    @property
    def royalty_info(self):
        return self._royalty_info

    @royalty_info.setter
    def royalty_info(self, value):
        if isinstance(value, list):
            self._royalty_info = list()
            for i in value:
                if isinstance(i, RoyaltyInfoRequest):
                    self._royalty_info.append(i)
                else:
                    self._royalty_info.append(RoyaltyInfoRequest.from_alipay_dict(i))
    @property
    def stage_no(self):
        return self._stage_no

    @stage_no.setter
    def stage_no(self, value):
        self._stage_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.royalty_info:
            if isinstance(self.royalty_info, list):
                for i in range(0, len(self.royalty_info)):
                    element = self.royalty_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.royalty_info[i] = element.to_alipay_dict()
            if hasattr(self.royalty_info, 'to_alipay_dict'):
                params['royalty_info'] = self.royalty_info.to_alipay_dict()
            else:
                params['royalty_info'] = self.royalty_info
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
        o = RentRoyaltyPublishDetailRequest()
        if 'royalty_info' in d:
            o.royalty_info = d['royalty_info']
        if 'stage_no' in d:
            o.stage_no = d['stage_no']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CplifeNoticeDetail import CplifeNoticeDetail


class AlipayEcoCplifeNoticePublishModel(object):

    def __init__(self):
        self._community_id_set = None
        self._notice_details = None

    @property
    def community_id_set(self):
        return self._community_id_set

    @community_id_set.setter
    def community_id_set(self, value):
        if isinstance(value, list):
            self._community_id_set = list()
            for i in value:
                self._community_id_set.append(i)
    @property
    def notice_details(self):
        return self._notice_details

    @notice_details.setter
    def notice_details(self, value):
        if isinstance(value, CplifeNoticeDetail):
            self._notice_details = value
        else:
            self._notice_details = CplifeNoticeDetail.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.community_id_set:
            if isinstance(self.community_id_set, list):
                for i in range(0, len(self.community_id_set)):
                    element = self.community_id_set[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.community_id_set[i] = element.to_alipay_dict()
            if hasattr(self.community_id_set, 'to_alipay_dict'):
                params['community_id_set'] = self.community_id_set.to_alipay_dict()
            else:
                params['community_id_set'] = self.community_id_set
        if self.notice_details:
            if hasattr(self.notice_details, 'to_alipay_dict'):
                params['notice_details'] = self.notice_details.to_alipay_dict()
            else:
                params['notice_details'] = self.notice_details
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoCplifeNoticePublishModel()
        if 'community_id_set' in d:
            o.community_id_set = d['community_id_set']
        if 'notice_details' in d:
            o.notice_details = d['notice_details']
        return o



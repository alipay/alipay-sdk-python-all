#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingCampaignMemberTemplateBatchqueryModel(object):

    def __init__(self):
        self._member_template_ids = None

    @property
    def member_template_ids(self):
        return self._member_template_ids

    @member_template_ids.setter
    def member_template_ids(self, value):
        if isinstance(value, list):
            self._member_template_ids = list()
            for i in value:
                self._member_template_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.member_template_ids:
            if isinstance(self.member_template_ids, list):
                for i in range(0, len(self.member_template_ids)):
                    element = self.member_template_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.member_template_ids[i] = element.to_alipay_dict()
            if hasattr(self.member_template_ids, 'to_alipay_dict'):
                params['member_template_ids'] = self.member_template_ids.to_alipay_dict()
            else:
                params['member_template_ids'] = self.member_template_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingCampaignMemberTemplateBatchqueryModel()
        if 'member_template_ids' in d:
            o.member_template_ids = d['member_template_ids']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantComplainGovernmentFinishModel(object):

    def __init__(self):
        self._complain_event_id = None
        self._finish_memo = None
        self._government_agency = None

    @property
    def complain_event_id(self):
        return self._complain_event_id

    @complain_event_id.setter
    def complain_event_id(self, value):
        self._complain_event_id = value
    @property
    def finish_memo(self):
        return self._finish_memo

    @finish_memo.setter
    def finish_memo(self, value):
        self._finish_memo = value
    @property
    def government_agency(self):
        return self._government_agency

    @government_agency.setter
    def government_agency(self, value):
        self._government_agency = value


    def to_alipay_dict(self):
        params = dict()
        if self.complain_event_id:
            if hasattr(self.complain_event_id, 'to_alipay_dict'):
                params['complain_event_id'] = self.complain_event_id.to_alipay_dict()
            else:
                params['complain_event_id'] = self.complain_event_id
        if self.finish_memo:
            if hasattr(self.finish_memo, 'to_alipay_dict'):
                params['finish_memo'] = self.finish_memo.to_alipay_dict()
            else:
                params['finish_memo'] = self.finish_memo
        if self.government_agency:
            if hasattr(self.government_agency, 'to_alipay_dict'):
                params['government_agency'] = self.government_agency.to_alipay_dict()
            else:
                params['government_agency'] = self.government_agency
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantComplainGovernmentFinishModel()
        if 'complain_event_id' in d:
            o.complain_event_id = d['complain_event_id']
        if 'finish_memo' in d:
            o.finish_memo = d['finish_memo']
        if 'government_agency' in d:
            o.government_agency = d['government_agency']
        return o



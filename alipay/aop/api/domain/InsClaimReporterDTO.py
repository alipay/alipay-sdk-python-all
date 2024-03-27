#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsClaimReporterDTO(object):

    def __init__(self):
        self._reporter_id_card_no = None
        self._reporter_name = None
        self._reporter_uid = None

    @property
    def reporter_id_card_no(self):
        return self._reporter_id_card_no

    @reporter_id_card_no.setter
    def reporter_id_card_no(self, value):
        self._reporter_id_card_no = value
    @property
    def reporter_name(self):
        return self._reporter_name

    @reporter_name.setter
    def reporter_name(self, value):
        self._reporter_name = value
    @property
    def reporter_uid(self):
        return self._reporter_uid

    @reporter_uid.setter
    def reporter_uid(self, value):
        self._reporter_uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.reporter_id_card_no:
            if hasattr(self.reporter_id_card_no, 'to_alipay_dict'):
                params['reporter_id_card_no'] = self.reporter_id_card_no.to_alipay_dict()
            else:
                params['reporter_id_card_no'] = self.reporter_id_card_no
        if self.reporter_name:
            if hasattr(self.reporter_name, 'to_alipay_dict'):
                params['reporter_name'] = self.reporter_name.to_alipay_dict()
            else:
                params['reporter_name'] = self.reporter_name
        if self.reporter_uid:
            if hasattr(self.reporter_uid, 'to_alipay_dict'):
                params['reporter_uid'] = self.reporter_uid.to_alipay_dict()
            else:
                params['reporter_uid'] = self.reporter_uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsClaimReporterDTO()
        if 'reporter_id_card_no' in d:
            o.reporter_id_card_no = d['reporter_id_card_no']
        if 'reporter_name' in d:
            o.reporter_name = d['reporter_name']
        if 'reporter_uid' in d:
            o.reporter_uid = d['reporter_uid']
        return o



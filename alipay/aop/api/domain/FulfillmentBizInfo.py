#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Advisory import Advisory
from alipay.aop.api.domain.Consultation import Consultation
from alipay.aop.api.domain.Examination import Examination


class FulfillmentBizInfo(object):

    def __init__(self):
        self._advisory = None
        self._consultation = None
        self._examination = None

    @property
    def advisory(self):
        return self._advisory

    @advisory.setter
    def advisory(self, value):
        if isinstance(value, Advisory):
            self._advisory = value
        else:
            self._advisory = Advisory.from_alipay_dict(value)
    @property
    def consultation(self):
        return self._consultation

    @consultation.setter
    def consultation(self, value):
        if isinstance(value, Consultation):
            self._consultation = value
        else:
            self._consultation = Consultation.from_alipay_dict(value)
    @property
    def examination(self):
        return self._examination

    @examination.setter
    def examination(self, value):
        if isinstance(value, Examination):
            self._examination = value
        else:
            self._examination = Examination.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.advisory:
            if hasattr(self.advisory, 'to_alipay_dict'):
                params['advisory'] = self.advisory.to_alipay_dict()
            else:
                params['advisory'] = self.advisory
        if self.consultation:
            if hasattr(self.consultation, 'to_alipay_dict'):
                params['consultation'] = self.consultation.to_alipay_dict()
            else:
                params['consultation'] = self.consultation
        if self.examination:
            if hasattr(self.examination, 'to_alipay_dict'):
                params['examination'] = self.examination.to_alipay_dict()
            else:
                params['examination'] = self.examination
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FulfillmentBizInfo()
        if 'advisory' in d:
            o.advisory = d['advisory']
        if 'consultation' in d:
            o.consultation = d['consultation']
        if 'examination' in d:
            o.examination = d['examination']
        return o



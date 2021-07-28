#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreditPayAssetBaseVO import CreditPayAssetBaseVO
from alipay.aop.api.domain.CreditPayCompensateDetailVO import CreditPayCompensateDetailVO


class CreditPayGuaranteeAssetVO(object):

    def __init__(self):
        self._base_info = None
        self._compensate_detail = None
        self._guar_term = None
        self._guar_term_type = None

    @property
    def base_info(self):
        return self._base_info

    @base_info.setter
    def base_info(self, value):
        if isinstance(value, CreditPayAssetBaseVO):
            self._base_info = value
        else:
            self._base_info = CreditPayAssetBaseVO.from_alipay_dict(value)
    @property
    def compensate_detail(self):
        return self._compensate_detail

    @compensate_detail.setter
    def compensate_detail(self, value):
        if isinstance(value, CreditPayCompensateDetailVO):
            self._compensate_detail = value
        else:
            self._compensate_detail = CreditPayCompensateDetailVO.from_alipay_dict(value)
    @property
    def guar_term(self):
        return self._guar_term

    @guar_term.setter
    def guar_term(self, value):
        self._guar_term = value
    @property
    def guar_term_type(self):
        return self._guar_term_type

    @guar_term_type.setter
    def guar_term_type(self, value):
        self._guar_term_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.base_info:
            if hasattr(self.base_info, 'to_alipay_dict'):
                params['base_info'] = self.base_info.to_alipay_dict()
            else:
                params['base_info'] = self.base_info
        if self.compensate_detail:
            if hasattr(self.compensate_detail, 'to_alipay_dict'):
                params['compensate_detail'] = self.compensate_detail.to_alipay_dict()
            else:
                params['compensate_detail'] = self.compensate_detail
        if self.guar_term:
            if hasattr(self.guar_term, 'to_alipay_dict'):
                params['guar_term'] = self.guar_term.to_alipay_dict()
            else:
                params['guar_term'] = self.guar_term
        if self.guar_term_type:
            if hasattr(self.guar_term_type, 'to_alipay_dict'):
                params['guar_term_type'] = self.guar_term_type.to_alipay_dict()
            else:
                params['guar_term_type'] = self.guar_term_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditPayGuaranteeAssetVO()
        if 'base_info' in d:
            o.base_info = d['base_info']
        if 'compensate_detail' in d:
            o.compensate_detail = d['compensate_detail']
        if 'guar_term' in d:
            o.guar_term = d['guar_term']
        if 'guar_term_type' in d:
            o.guar_term_type = d['guar_term_type']
        return o



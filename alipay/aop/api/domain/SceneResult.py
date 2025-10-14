#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AACProspectFlashSaleResult import AACProspectFlashSaleResult


class SceneResult(object):

    def __init__(self):
        self._aac_prospect_flash_sale = None

    @property
    def aac_prospect_flash_sale(self):
        return self._aac_prospect_flash_sale

    @aac_prospect_flash_sale.setter
    def aac_prospect_flash_sale(self, value):
        if isinstance(value, AACProspectFlashSaleResult):
            self._aac_prospect_flash_sale = value
        else:
            self._aac_prospect_flash_sale = AACProspectFlashSaleResult.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.aac_prospect_flash_sale:
            if hasattr(self.aac_prospect_flash_sale, 'to_alipay_dict'):
                params['aac_prospect_flash_sale'] = self.aac_prospect_flash_sale.to_alipay_dict()
            else:
                params['aac_prospect_flash_sale'] = self.aac_prospect_flash_sale
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SceneResult()
        if 'aac_prospect_flash_sale' in d:
            o.aac_prospect_flash_sale = d['aac_prospect_flash_sale']
        return o



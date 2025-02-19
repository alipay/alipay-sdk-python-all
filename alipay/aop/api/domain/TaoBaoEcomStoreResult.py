#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PenCaseInfo import PenCaseInfo
from alipay.aop.api.domain.TaoBaoEcomStoreInfo import TaoBaoEcomStoreInfo
from alipay.aop.api.domain.FrShopIndexInfo import FrShopIndexInfo
from alipay.aop.api.domain.PunishBreakInfo import PunishBreakInfo
from alipay.aop.api.domain.PunishedInfo import PunishedInfo
from alipay.aop.api.domain.RelatedPerformanceInfo import RelatedPerformanceInfo


class TaoBaoEcomStoreResult(object):

    def __init__(self):
        self._case_info_list = None
        self._ecom_shop_info = None
        self._fr_shop_index_info = None
        self._punish_break_list = None
        self._punished_list = None
        self._ry_pos_fr_list = None

    @property
    def case_info_list(self):
        return self._case_info_list

    @case_info_list.setter
    def case_info_list(self, value):
        if isinstance(value, list):
            self._case_info_list = list()
            for i in value:
                if isinstance(i, PenCaseInfo):
                    self._case_info_list.append(i)
                else:
                    self._case_info_list.append(PenCaseInfo.from_alipay_dict(i))
    @property
    def ecom_shop_info(self):
        return self._ecom_shop_info

    @ecom_shop_info.setter
    def ecom_shop_info(self, value):
        if isinstance(value, list):
            self._ecom_shop_info = list()
            for i in value:
                if isinstance(i, TaoBaoEcomStoreInfo):
                    self._ecom_shop_info.append(i)
                else:
                    self._ecom_shop_info.append(TaoBaoEcomStoreInfo.from_alipay_dict(i))
    @property
    def fr_shop_index_info(self):
        return self._fr_shop_index_info

    @fr_shop_index_info.setter
    def fr_shop_index_info(self, value):
        if isinstance(value, FrShopIndexInfo):
            self._fr_shop_index_info = value
        else:
            self._fr_shop_index_info = FrShopIndexInfo.from_alipay_dict(value)
    @property
    def punish_break_list(self):
        return self._punish_break_list

    @punish_break_list.setter
    def punish_break_list(self, value):
        if isinstance(value, list):
            self._punish_break_list = list()
            for i in value:
                if isinstance(i, PunishBreakInfo):
                    self._punish_break_list.append(i)
                else:
                    self._punish_break_list.append(PunishBreakInfo.from_alipay_dict(i))
    @property
    def punished_list(self):
        return self._punished_list

    @punished_list.setter
    def punished_list(self, value):
        if isinstance(value, list):
            self._punished_list = list()
            for i in value:
                if isinstance(i, PunishedInfo):
                    self._punished_list.append(i)
                else:
                    self._punished_list.append(PunishedInfo.from_alipay_dict(i))
    @property
    def ry_pos_fr_list(self):
        return self._ry_pos_fr_list

    @ry_pos_fr_list.setter
    def ry_pos_fr_list(self, value):
        if isinstance(value, list):
            self._ry_pos_fr_list = list()
            for i in value:
                if isinstance(i, RelatedPerformanceInfo):
                    self._ry_pos_fr_list.append(i)
                else:
                    self._ry_pos_fr_list.append(RelatedPerformanceInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.case_info_list:
            if isinstance(self.case_info_list, list):
                for i in range(0, len(self.case_info_list)):
                    element = self.case_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.case_info_list[i] = element.to_alipay_dict()
            if hasattr(self.case_info_list, 'to_alipay_dict'):
                params['case_info_list'] = self.case_info_list.to_alipay_dict()
            else:
                params['case_info_list'] = self.case_info_list
        if self.ecom_shop_info:
            if isinstance(self.ecom_shop_info, list):
                for i in range(0, len(self.ecom_shop_info)):
                    element = self.ecom_shop_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ecom_shop_info[i] = element.to_alipay_dict()
            if hasattr(self.ecom_shop_info, 'to_alipay_dict'):
                params['ecom_shop_info'] = self.ecom_shop_info.to_alipay_dict()
            else:
                params['ecom_shop_info'] = self.ecom_shop_info
        if self.fr_shop_index_info:
            if hasattr(self.fr_shop_index_info, 'to_alipay_dict'):
                params['fr_shop_index_info'] = self.fr_shop_index_info.to_alipay_dict()
            else:
                params['fr_shop_index_info'] = self.fr_shop_index_info
        if self.punish_break_list:
            if isinstance(self.punish_break_list, list):
                for i in range(0, len(self.punish_break_list)):
                    element = self.punish_break_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.punish_break_list[i] = element.to_alipay_dict()
            if hasattr(self.punish_break_list, 'to_alipay_dict'):
                params['punish_break_list'] = self.punish_break_list.to_alipay_dict()
            else:
                params['punish_break_list'] = self.punish_break_list
        if self.punished_list:
            if isinstance(self.punished_list, list):
                for i in range(0, len(self.punished_list)):
                    element = self.punished_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.punished_list[i] = element.to_alipay_dict()
            if hasattr(self.punished_list, 'to_alipay_dict'):
                params['punished_list'] = self.punished_list.to_alipay_dict()
            else:
                params['punished_list'] = self.punished_list
        if self.ry_pos_fr_list:
            if isinstance(self.ry_pos_fr_list, list):
                for i in range(0, len(self.ry_pos_fr_list)):
                    element = self.ry_pos_fr_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ry_pos_fr_list[i] = element.to_alipay_dict()
            if hasattr(self.ry_pos_fr_list, 'to_alipay_dict'):
                params['ry_pos_fr_list'] = self.ry_pos_fr_list.to_alipay_dict()
            else:
                params['ry_pos_fr_list'] = self.ry_pos_fr_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TaoBaoEcomStoreResult()
        if 'case_info_list' in d:
            o.case_info_list = d['case_info_list']
        if 'ecom_shop_info' in d:
            o.ecom_shop_info = d['ecom_shop_info']
        if 'fr_shop_index_info' in d:
            o.fr_shop_index_info = d['fr_shop_index_info']
        if 'punish_break_list' in d:
            o.punish_break_list = d['punish_break_list']
        if 'punished_list' in d:
            o.punished_list = d['punished_list']
        if 'ry_pos_fr_list' in d:
            o.ry_pos_fr_list = d['ry_pos_fr_list']
        return o



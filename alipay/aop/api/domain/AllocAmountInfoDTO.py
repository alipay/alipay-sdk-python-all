#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RoyaltyDTO import RoyaltyDTO
from alipay.aop.api.domain.RentRoyaltyDetailDTO import RentRoyaltyDetailDTO


class AllocAmountInfoDTO(object):

    def __init__(self):
        self._buy_out_royalty = None
        self._invest_app_id = None
        self._invest_id = None
        self._rent_royalty_details = None

    @property
    def buy_out_royalty(self):
        return self._buy_out_royalty

    @buy_out_royalty.setter
    def buy_out_royalty(self, value):
        if isinstance(value, RoyaltyDTO):
            self._buy_out_royalty = value
        else:
            self._buy_out_royalty = RoyaltyDTO.from_alipay_dict(value)
    @property
    def invest_app_id(self):
        return self._invest_app_id

    @invest_app_id.setter
    def invest_app_id(self, value):
        self._invest_app_id = value
    @property
    def invest_id(self):
        return self._invest_id

    @invest_id.setter
    def invest_id(self, value):
        self._invest_id = value
    @property
    def rent_royalty_details(self):
        return self._rent_royalty_details

    @rent_royalty_details.setter
    def rent_royalty_details(self, value):
        if isinstance(value, list):
            self._rent_royalty_details = list()
            for i in value:
                if isinstance(i, RentRoyaltyDetailDTO):
                    self._rent_royalty_details.append(i)
                else:
                    self._rent_royalty_details.append(RentRoyaltyDetailDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.buy_out_royalty:
            if hasattr(self.buy_out_royalty, 'to_alipay_dict'):
                params['buy_out_royalty'] = self.buy_out_royalty.to_alipay_dict()
            else:
                params['buy_out_royalty'] = self.buy_out_royalty
        if self.invest_app_id:
            if hasattr(self.invest_app_id, 'to_alipay_dict'):
                params['invest_app_id'] = self.invest_app_id.to_alipay_dict()
            else:
                params['invest_app_id'] = self.invest_app_id
        if self.invest_id:
            if hasattr(self.invest_id, 'to_alipay_dict'):
                params['invest_id'] = self.invest_id.to_alipay_dict()
            else:
                params['invest_id'] = self.invest_id
        if self.rent_royalty_details:
            if isinstance(self.rent_royalty_details, list):
                for i in range(0, len(self.rent_royalty_details)):
                    element = self.rent_royalty_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rent_royalty_details[i] = element.to_alipay_dict()
            if hasattr(self.rent_royalty_details, 'to_alipay_dict'):
                params['rent_royalty_details'] = self.rent_royalty_details.to_alipay_dict()
            else:
                params['rent_royalty_details'] = self.rent_royalty_details
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AllocAmountInfoDTO()
        if 'buy_out_royalty' in d:
            o.buy_out_royalty = d['buy_out_royalty']
        if 'invest_app_id' in d:
            o.invest_app_id = d['invest_app_id']
        if 'invest_id' in d:
            o.invest_id = d['invest_id']
        if 'rent_royalty_details' in d:
            o.rent_royalty_details = d['rent_royalty_details']
        return o



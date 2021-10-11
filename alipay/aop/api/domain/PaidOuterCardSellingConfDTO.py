#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PaidOuterCardPriceDetailDTO import PaidOuterCardPriceDetailDTO


class PaidOuterCardSellingConfDTO(object):

    def __init__(self):
        self._end_date = None
        self._price_detail = None
        self._selling_url = None
        self._start_date = None

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def price_detail(self):
        return self._price_detail

    @price_detail.setter
    def price_detail(self, value):
        if isinstance(value, list):
            self._price_detail = list()
            for i in value:
                if isinstance(i, PaidOuterCardPriceDetailDTO):
                    self._price_detail.append(i)
                else:
                    self._price_detail.append(PaidOuterCardPriceDetailDTO.from_alipay_dict(i))
    @property
    def selling_url(self):
        return self._selling_url

    @selling_url.setter
    def selling_url(self, value):
        self._selling_url = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.price_detail:
            if isinstance(self.price_detail, list):
                for i in range(0, len(self.price_detail)):
                    element = self.price_detail[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.price_detail[i] = element.to_alipay_dict()
            if hasattr(self.price_detail, 'to_alipay_dict'):
                params['price_detail'] = self.price_detail.to_alipay_dict()
            else:
                params['price_detail'] = self.price_detail
        if self.selling_url:
            if hasattr(self.selling_url, 'to_alipay_dict'):
                params['selling_url'] = self.selling_url.to_alipay_dict()
            else:
                params['selling_url'] = self.selling_url
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaidOuterCardSellingConfDTO()
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'price_detail' in d:
            o.price_detail = d['price_detail']
        if 'selling_url' in d:
            o.selling_url = d['selling_url']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o



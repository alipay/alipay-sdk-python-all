#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FulfillmentItemPdfInfo import FulfillmentItemPdfInfo


class ExaminationParam(object):

    def __init__(self):
        self._item_id_to_pdf = None

    @property
    def item_id_to_pdf(self):
        return self._item_id_to_pdf

    @item_id_to_pdf.setter
    def item_id_to_pdf(self, value):
        if isinstance(value, list):
            self._item_id_to_pdf = list()
            for i in value:
                if isinstance(i, FulfillmentItemPdfInfo):
                    self._item_id_to_pdf.append(i)
                else:
                    self._item_id_to_pdf.append(FulfillmentItemPdfInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.item_id_to_pdf:
            if isinstance(self.item_id_to_pdf, list):
                for i in range(0, len(self.item_id_to_pdf)):
                    element = self.item_id_to_pdf[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_id_to_pdf[i] = element.to_alipay_dict()
            if hasattr(self.item_id_to_pdf, 'to_alipay_dict'):
                params['item_id_to_pdf'] = self.item_id_to_pdf.to_alipay_dict()
            else:
                params['item_id_to_pdf'] = self.item_id_to_pdf
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExaminationParam()
        if 'item_id_to_pdf' in d:
            o.item_id_to_pdf = d['item_id_to_pdf']
        return o



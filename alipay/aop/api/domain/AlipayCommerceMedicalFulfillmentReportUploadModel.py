#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FulfillmentReportInfoDTO import FulfillmentReportInfoDTO


class AlipayCommerceMedicalFulfillmentReportUploadModel(object):

    def __init__(self):
        self._fulfillment_id = None
        self._report_infos = None
        self._trade_order_id = None

    @property
    def fulfillment_id(self):
        return self._fulfillment_id

    @fulfillment_id.setter
    def fulfillment_id(self, value):
        self._fulfillment_id = value
    @property
    def report_infos(self):
        return self._report_infos

    @report_infos.setter
    def report_infos(self, value):
        if isinstance(value, list):
            self._report_infos = list()
            for i in value:
                if isinstance(i, FulfillmentReportInfoDTO):
                    self._report_infos.append(i)
                else:
                    self._report_infos.append(FulfillmentReportInfoDTO.from_alipay_dict(i))
    @property
    def trade_order_id(self):
        return self._trade_order_id

    @trade_order_id.setter
    def trade_order_id(self, value):
        self._trade_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.fulfillment_id:
            if hasattr(self.fulfillment_id, 'to_alipay_dict'):
                params['fulfillment_id'] = self.fulfillment_id.to_alipay_dict()
            else:
                params['fulfillment_id'] = self.fulfillment_id
        if self.report_infos:
            if isinstance(self.report_infos, list):
                for i in range(0, len(self.report_infos)):
                    element = self.report_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.report_infos[i] = element.to_alipay_dict()
            if hasattr(self.report_infos, 'to_alipay_dict'):
                params['report_infos'] = self.report_infos.to_alipay_dict()
            else:
                params['report_infos'] = self.report_infos
        if self.trade_order_id:
            if hasattr(self.trade_order_id, 'to_alipay_dict'):
                params['trade_order_id'] = self.trade_order_id.to_alipay_dict()
            else:
                params['trade_order_id'] = self.trade_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalFulfillmentReportUploadModel()
        if 'fulfillment_id' in d:
            o.fulfillment_id = d['fulfillment_id']
        if 'report_infos' in d:
            o.report_infos = d['report_infos']
        if 'trade_order_id' in d:
            o.trade_order_id = d['trade_order_id']
        return o



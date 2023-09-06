#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceArrivalDTO import InvoiceArrivalDTO
from alipay.aop.api.domain.InvoiceDTO import InvoiceDTO


class InvoiceSpecificsDTO(object):

    def __init__(self):
        self._invoice_arrival_dtos = None
        self._invoice_dto = None

    @property
    def invoice_arrival_dtos(self):
        return self._invoice_arrival_dtos

    @invoice_arrival_dtos.setter
    def invoice_arrival_dtos(self, value):
        if isinstance(value, list):
            self._invoice_arrival_dtos = list()
            for i in value:
                if isinstance(i, InvoiceArrivalDTO):
                    self._invoice_arrival_dtos.append(i)
                else:
                    self._invoice_arrival_dtos.append(InvoiceArrivalDTO.from_alipay_dict(i))
    @property
    def invoice_dto(self):
        return self._invoice_dto

    @invoice_dto.setter
    def invoice_dto(self, value):
        if isinstance(value, InvoiceDTO):
            self._invoice_dto = value
        else:
            self._invoice_dto = InvoiceDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.invoice_arrival_dtos:
            if isinstance(self.invoice_arrival_dtos, list):
                for i in range(0, len(self.invoice_arrival_dtos)):
                    element = self.invoice_arrival_dtos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_arrival_dtos[i] = element.to_alipay_dict()
            if hasattr(self.invoice_arrival_dtos, 'to_alipay_dict'):
                params['invoice_arrival_dtos'] = self.invoice_arrival_dtos.to_alipay_dict()
            else:
                params['invoice_arrival_dtos'] = self.invoice_arrival_dtos
        if self.invoice_dto:
            if hasattr(self.invoice_dto, 'to_alipay_dict'):
                params['invoice_dto'] = self.invoice_dto.to_alipay_dict()
            else:
                params['invoice_dto'] = self.invoice_dto
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceSpecificsDTO()
        if 'invoice_arrival_dtos' in d:
            o.invoice_arrival_dtos = d['invoice_arrival_dtos']
        if 'invoice_dto' in d:
            o.invoice_dto = d['invoice_dto']
        return o



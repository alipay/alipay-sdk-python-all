#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceInfoOpenApiDTO import InvoiceInfoOpenApiDTO


class InvoiceInfoOpenApiResponseDTO(object):

    def __init__(self):
        self._invoice_info_open_api_dto_list = None

    @property
    def invoice_info_open_api_dto_list(self):
        return self._invoice_info_open_api_dto_list

    @invoice_info_open_api_dto_list.setter
    def invoice_info_open_api_dto_list(self, value):
        if isinstance(value, list):
            self._invoice_info_open_api_dto_list = list()
            for i in value:
                if isinstance(i, InvoiceInfoOpenApiDTO):
                    self._invoice_info_open_api_dto_list.append(i)
                else:
                    self._invoice_info_open_api_dto_list.append(InvoiceInfoOpenApiDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.invoice_info_open_api_dto_list:
            if isinstance(self.invoice_info_open_api_dto_list, list):
                for i in range(0, len(self.invoice_info_open_api_dto_list)):
                    element = self.invoice_info_open_api_dto_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_info_open_api_dto_list[i] = element.to_alipay_dict()
            if hasattr(self.invoice_info_open_api_dto_list, 'to_alipay_dict'):
                params['invoice_info_open_api_dto_list'] = self.invoice_info_open_api_dto_list.to_alipay_dict()
            else:
                params['invoice_info_open_api_dto_list'] = self.invoice_info_open_api_dto_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceInfoOpenApiResponseDTO()
        if 'invoice_info_open_api_dto_list' in d:
            o.invoice_info_open_api_dto_list = d['invoice_info_open_api_dto_list']
        return o



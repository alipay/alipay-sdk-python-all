#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TemplateEInfoDTO import TemplateEInfoDTO
from alipay.aop.api.domain.TemplateOperationDTO import TemplateOperationDTO
from alipay.aop.api.domain.TemplateProfitDTO import TemplateProfitDTO
from alipay.aop.api.domain.TemplateRemindDTO import TemplateRemindDTO
from alipay.aop.api.domain.TemplateSecondaryOperationDTO import TemplateSecondaryOperationDTO


class TemplateEvoucherDTO(object):

    def __init__(self):
        self._einfo = None
        self._end_date = None
        self._operations = None
        self._pass_sub_type = None
        self._product = None
        self._profit = None
        self._remind_info = None
        self._secondary_operation = None
        self._start_date = None
        self._title = None
        self._type = None

    @property
    def einfo(self):
        return self._einfo

    @einfo.setter
    def einfo(self, value):
        if isinstance(value, TemplateEInfoDTO):
            self._einfo = value
        else:
            self._einfo = TemplateEInfoDTO.from_alipay_dict(value)
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def operations(self):
        return self._operations

    @operations.setter
    def operations(self, value):
        if isinstance(value, list):
            self._operations = list()
            for i in value:
                if isinstance(i, TemplateOperationDTO):
                    self._operations.append(i)
                else:
                    self._operations.append(TemplateOperationDTO.from_alipay_dict(i))
    @property
    def pass_sub_type(self):
        return self._pass_sub_type

    @pass_sub_type.setter
    def pass_sub_type(self, value):
        self._pass_sub_type = value
    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        self._product = value
    @property
    def profit(self):
        return self._profit

    @profit.setter
    def profit(self, value):
        if isinstance(value, TemplateProfitDTO):
            self._profit = value
        else:
            self._profit = TemplateProfitDTO.from_alipay_dict(value)
    @property
    def remind_info(self):
        return self._remind_info

    @remind_info.setter
    def remind_info(self, value):
        if isinstance(value, TemplateRemindDTO):
            self._remind_info = value
        else:
            self._remind_info = TemplateRemindDTO.from_alipay_dict(value)
    @property
    def secondary_operation(self):
        return self._secondary_operation

    @secondary_operation.setter
    def secondary_operation(self, value):
        if isinstance(value, TemplateSecondaryOperationDTO):
            self._secondary_operation = value
        else:
            self._secondary_operation = TemplateSecondaryOperationDTO.from_alipay_dict(value)
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.einfo:
            if hasattr(self.einfo, 'to_alipay_dict'):
                params['einfo'] = self.einfo.to_alipay_dict()
            else:
                params['einfo'] = self.einfo
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.operations:
            if isinstance(self.operations, list):
                for i in range(0, len(self.operations)):
                    element = self.operations[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.operations[i] = element.to_alipay_dict()
            if hasattr(self.operations, 'to_alipay_dict'):
                params['operations'] = self.operations.to_alipay_dict()
            else:
                params['operations'] = self.operations
        if self.pass_sub_type:
            if hasattr(self.pass_sub_type, 'to_alipay_dict'):
                params['pass_sub_type'] = self.pass_sub_type.to_alipay_dict()
            else:
                params['pass_sub_type'] = self.pass_sub_type
        if self.product:
            if hasattr(self.product, 'to_alipay_dict'):
                params['product'] = self.product.to_alipay_dict()
            else:
                params['product'] = self.product
        if self.profit:
            if hasattr(self.profit, 'to_alipay_dict'):
                params['profit'] = self.profit.to_alipay_dict()
            else:
                params['profit'] = self.profit
        if self.remind_info:
            if hasattr(self.remind_info, 'to_alipay_dict'):
                params['remind_info'] = self.remind_info.to_alipay_dict()
            else:
                params['remind_info'] = self.remind_info
        if self.secondary_operation:
            if hasattr(self.secondary_operation, 'to_alipay_dict'):
                params['secondary_operation'] = self.secondary_operation.to_alipay_dict()
            else:
                params['secondary_operation'] = self.secondary_operation
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TemplateEvoucherDTO()
        if 'einfo' in d:
            o.einfo = d['einfo']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'operations' in d:
            o.operations = d['operations']
        if 'pass_sub_type' in d:
            o.pass_sub_type = d['pass_sub_type']
        if 'product' in d:
            o.product = d['product']
        if 'profit' in d:
            o.profit = d['profit']
        if 'remind_info' in d:
            o.remind_info = d['remind_info']
        if 'secondary_operation' in d:
            o.secondary_operation = d['secondary_operation']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'title' in d:
            o.title = d['title']
        if 'type' in d:
            o.type = d['type']
        return o



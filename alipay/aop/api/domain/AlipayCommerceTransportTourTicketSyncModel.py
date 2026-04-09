#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TourTicketInfo import TourTicketInfo


class AlipayCommerceTransportTourTicketSyncModel(object):

    def __init__(self):
        self._scenic_id = None
        self._ticket_info_list = None

    @property
    def scenic_id(self):
        return self._scenic_id

    @scenic_id.setter
    def scenic_id(self, value):
        self._scenic_id = value
    @property
    def ticket_info_list(self):
        return self._ticket_info_list

    @ticket_info_list.setter
    def ticket_info_list(self, value):
        if isinstance(value, list):
            self._ticket_info_list = list()
            for i in value:
                if isinstance(i, TourTicketInfo):
                    self._ticket_info_list.append(i)
                else:
                    self._ticket_info_list.append(TourTicketInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.scenic_id:
            if hasattr(self.scenic_id, 'to_alipay_dict'):
                params['scenic_id'] = self.scenic_id.to_alipay_dict()
            else:
                params['scenic_id'] = self.scenic_id
        if self.ticket_info_list:
            if isinstance(self.ticket_info_list, list):
                for i in range(0, len(self.ticket_info_list)):
                    element = self.ticket_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ticket_info_list[i] = element.to_alipay_dict()
            if hasattr(self.ticket_info_list, 'to_alipay_dict'):
                params['ticket_info_list'] = self.ticket_info_list.to_alipay_dict()
            else:
                params['ticket_info_list'] = self.ticket_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportTourTicketSyncModel()
        if 'scenic_id' in d:
            o.scenic_id = d['scenic_id']
        if 'ticket_info_list' in d:
            o.ticket_info_list = d['ticket_info_list']
        return o



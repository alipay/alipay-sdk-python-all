#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TrafficAirticketOrderCommodityInfo import TrafficAirticketOrderCommodityInfo
from alipay.aop.api.domain.TrafficAirticketOrderShareInfo import TrafficAirticketOrderShareInfo


class TrafficAirticketOrderTicketInfo(object):

    def __init__(self):
        self._arr_airport_code = None
        self._arr_airport_name = None
        self._arr_city_code = None
        self._arr_city_name = None
        self._arr_time = None
        self._commodity_info_list = None
        self._dep_airport_code = None
        self._dep_airport_name = None
        self._dep_city_code = None
        self._dep_city_name = None
        self._dep_time = None
        self._international = None
        self._ori_ticket_uuid = None
        self._share = None
        self._share_info = None
        self._status = None
        self._status_desc = None
        self._ticket_no = None
        self._ticket_order = None
        self._ticket_type = None
        self._ticket_uuid = None

    @property
    def arr_airport_code(self):
        return self._arr_airport_code

    @arr_airport_code.setter
    def arr_airport_code(self, value):
        self._arr_airport_code = value
    @property
    def arr_airport_name(self):
        return self._arr_airport_name

    @arr_airport_name.setter
    def arr_airport_name(self, value):
        self._arr_airport_name = value
    @property
    def arr_city_code(self):
        return self._arr_city_code

    @arr_city_code.setter
    def arr_city_code(self, value):
        self._arr_city_code = value
    @property
    def arr_city_name(self):
        return self._arr_city_name

    @arr_city_name.setter
    def arr_city_name(self, value):
        self._arr_city_name = value
    @property
    def arr_time(self):
        return self._arr_time

    @arr_time.setter
    def arr_time(self, value):
        self._arr_time = value
    @property
    def commodity_info_list(self):
        return self._commodity_info_list

    @commodity_info_list.setter
    def commodity_info_list(self, value):
        if isinstance(value, list):
            self._commodity_info_list = list()
            for i in value:
                if isinstance(i, TrafficAirticketOrderCommodityInfo):
                    self._commodity_info_list.append(i)
                else:
                    self._commodity_info_list.append(TrafficAirticketOrderCommodityInfo.from_alipay_dict(i))
    @property
    def dep_airport_code(self):
        return self._dep_airport_code

    @dep_airport_code.setter
    def dep_airport_code(self, value):
        self._dep_airport_code = value
    @property
    def dep_airport_name(self):
        return self._dep_airport_name

    @dep_airport_name.setter
    def dep_airport_name(self, value):
        self._dep_airport_name = value
    @property
    def dep_city_code(self):
        return self._dep_city_code

    @dep_city_code.setter
    def dep_city_code(self, value):
        self._dep_city_code = value
    @property
    def dep_city_name(self):
        return self._dep_city_name

    @dep_city_name.setter
    def dep_city_name(self, value):
        self._dep_city_name = value
    @property
    def dep_time(self):
        return self._dep_time

    @dep_time.setter
    def dep_time(self, value):
        self._dep_time = value
    @property
    def international(self):
        return self._international

    @international.setter
    def international(self, value):
        self._international = value
    @property
    def ori_ticket_uuid(self):
        return self._ori_ticket_uuid

    @ori_ticket_uuid.setter
    def ori_ticket_uuid(self, value):
        self._ori_ticket_uuid = value
    @property
    def share(self):
        return self._share

    @share.setter
    def share(self, value):
        self._share = value
    @property
    def share_info(self):
        return self._share_info

    @share_info.setter
    def share_info(self, value):
        if isinstance(value, TrafficAirticketOrderShareInfo):
            self._share_info = value
        else:
            self._share_info = TrafficAirticketOrderShareInfo.from_alipay_dict(value)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_desc(self):
        return self._status_desc

    @status_desc.setter
    def status_desc(self, value):
        self._status_desc = value
    @property
    def ticket_no(self):
        return self._ticket_no

    @ticket_no.setter
    def ticket_no(self, value):
        self._ticket_no = value
    @property
    def ticket_order(self):
        return self._ticket_order

    @ticket_order.setter
    def ticket_order(self, value):
        self._ticket_order = value
    @property
    def ticket_type(self):
        return self._ticket_type

    @ticket_type.setter
    def ticket_type(self, value):
        self._ticket_type = value
    @property
    def ticket_uuid(self):
        return self._ticket_uuid

    @ticket_uuid.setter
    def ticket_uuid(self, value):
        self._ticket_uuid = value


    def to_alipay_dict(self):
        params = dict()
        if self.arr_airport_code:
            if hasattr(self.arr_airport_code, 'to_alipay_dict'):
                params['arr_airport_code'] = self.arr_airport_code.to_alipay_dict()
            else:
                params['arr_airport_code'] = self.arr_airport_code
        if self.arr_airport_name:
            if hasattr(self.arr_airport_name, 'to_alipay_dict'):
                params['arr_airport_name'] = self.arr_airport_name.to_alipay_dict()
            else:
                params['arr_airport_name'] = self.arr_airport_name
        if self.arr_city_code:
            if hasattr(self.arr_city_code, 'to_alipay_dict'):
                params['arr_city_code'] = self.arr_city_code.to_alipay_dict()
            else:
                params['arr_city_code'] = self.arr_city_code
        if self.arr_city_name:
            if hasattr(self.arr_city_name, 'to_alipay_dict'):
                params['arr_city_name'] = self.arr_city_name.to_alipay_dict()
            else:
                params['arr_city_name'] = self.arr_city_name
        if self.arr_time:
            if hasattr(self.arr_time, 'to_alipay_dict'):
                params['arr_time'] = self.arr_time.to_alipay_dict()
            else:
                params['arr_time'] = self.arr_time
        if self.commodity_info_list:
            if isinstance(self.commodity_info_list, list):
                for i in range(0, len(self.commodity_info_list)):
                    element = self.commodity_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.commodity_info_list[i] = element.to_alipay_dict()
            if hasattr(self.commodity_info_list, 'to_alipay_dict'):
                params['commodity_info_list'] = self.commodity_info_list.to_alipay_dict()
            else:
                params['commodity_info_list'] = self.commodity_info_list
        if self.dep_airport_code:
            if hasattr(self.dep_airport_code, 'to_alipay_dict'):
                params['dep_airport_code'] = self.dep_airport_code.to_alipay_dict()
            else:
                params['dep_airport_code'] = self.dep_airport_code
        if self.dep_airport_name:
            if hasattr(self.dep_airport_name, 'to_alipay_dict'):
                params['dep_airport_name'] = self.dep_airport_name.to_alipay_dict()
            else:
                params['dep_airport_name'] = self.dep_airport_name
        if self.dep_city_code:
            if hasattr(self.dep_city_code, 'to_alipay_dict'):
                params['dep_city_code'] = self.dep_city_code.to_alipay_dict()
            else:
                params['dep_city_code'] = self.dep_city_code
        if self.dep_city_name:
            if hasattr(self.dep_city_name, 'to_alipay_dict'):
                params['dep_city_name'] = self.dep_city_name.to_alipay_dict()
            else:
                params['dep_city_name'] = self.dep_city_name
        if self.dep_time:
            if hasattr(self.dep_time, 'to_alipay_dict'):
                params['dep_time'] = self.dep_time.to_alipay_dict()
            else:
                params['dep_time'] = self.dep_time
        if self.international:
            if hasattr(self.international, 'to_alipay_dict'):
                params['international'] = self.international.to_alipay_dict()
            else:
                params['international'] = self.international
        if self.ori_ticket_uuid:
            if hasattr(self.ori_ticket_uuid, 'to_alipay_dict'):
                params['ori_ticket_uuid'] = self.ori_ticket_uuid.to_alipay_dict()
            else:
                params['ori_ticket_uuid'] = self.ori_ticket_uuid
        if self.share:
            if hasattr(self.share, 'to_alipay_dict'):
                params['share'] = self.share.to_alipay_dict()
            else:
                params['share'] = self.share
        if self.share_info:
            if hasattr(self.share_info, 'to_alipay_dict'):
                params['share_info'] = self.share_info.to_alipay_dict()
            else:
                params['share_info'] = self.share_info
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.status_desc:
            if hasattr(self.status_desc, 'to_alipay_dict'):
                params['status_desc'] = self.status_desc.to_alipay_dict()
            else:
                params['status_desc'] = self.status_desc
        if self.ticket_no:
            if hasattr(self.ticket_no, 'to_alipay_dict'):
                params['ticket_no'] = self.ticket_no.to_alipay_dict()
            else:
                params['ticket_no'] = self.ticket_no
        if self.ticket_order:
            if hasattr(self.ticket_order, 'to_alipay_dict'):
                params['ticket_order'] = self.ticket_order.to_alipay_dict()
            else:
                params['ticket_order'] = self.ticket_order
        if self.ticket_type:
            if hasattr(self.ticket_type, 'to_alipay_dict'):
                params['ticket_type'] = self.ticket_type.to_alipay_dict()
            else:
                params['ticket_type'] = self.ticket_type
        if self.ticket_uuid:
            if hasattr(self.ticket_uuid, 'to_alipay_dict'):
                params['ticket_uuid'] = self.ticket_uuid.to_alipay_dict()
            else:
                params['ticket_uuid'] = self.ticket_uuid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TrafficAirticketOrderTicketInfo()
        if 'arr_airport_code' in d:
            o.arr_airport_code = d['arr_airport_code']
        if 'arr_airport_name' in d:
            o.arr_airport_name = d['arr_airport_name']
        if 'arr_city_code' in d:
            o.arr_city_code = d['arr_city_code']
        if 'arr_city_name' in d:
            o.arr_city_name = d['arr_city_name']
        if 'arr_time' in d:
            o.arr_time = d['arr_time']
        if 'commodity_info_list' in d:
            o.commodity_info_list = d['commodity_info_list']
        if 'dep_airport_code' in d:
            o.dep_airport_code = d['dep_airport_code']
        if 'dep_airport_name' in d:
            o.dep_airport_name = d['dep_airport_name']
        if 'dep_city_code' in d:
            o.dep_city_code = d['dep_city_code']
        if 'dep_city_name' in d:
            o.dep_city_name = d['dep_city_name']
        if 'dep_time' in d:
            o.dep_time = d['dep_time']
        if 'international' in d:
            o.international = d['international']
        if 'ori_ticket_uuid' in d:
            o.ori_ticket_uuid = d['ori_ticket_uuid']
        if 'share' in d:
            o.share = d['share']
        if 'share_info' in d:
            o.share_info = d['share_info']
        if 'status' in d:
            o.status = d['status']
        if 'status_desc' in d:
            o.status_desc = d['status_desc']
        if 'ticket_no' in d:
            o.ticket_no = d['ticket_no']
        if 'ticket_order' in d:
            o.ticket_order = d['ticket_order']
        if 'ticket_type' in d:
            o.ticket_type = d['ticket_type']
        if 'ticket_uuid' in d:
            o.ticket_uuid = d['ticket_uuid']
        return o



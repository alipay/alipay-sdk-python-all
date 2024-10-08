#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TrafficAirticketOrderCommodityInfo import TrafficAirticketOrderCommodityInfo
from alipay.aop.api.domain.TrafficAirticketOrderStopInfo import TrafficAirticketOrderStopInfo
from alipay.aop.api.domain.TrafficAirticketOrderTicketInfo import TrafficAirticketOrderTicketInfo


class TrafficAirticketOrderSegmentInfo(object):

    def __init__(self):
        self._ac_code = None
        self._ac_name = None
        self._arr_airport_code = None
        self._arr_airport_name = None
        self._arr_city_code = None
        self._arr_city_name = None
        self._arr_terminal = None
        self._arr_time = None
        self._cabin_code = None
        self._cabin_name = None
        self._commodity_info_list = None
        self._dep_airport_code = None
        self._dep_airport_name = None
        self._dep_city_code = None
        self._dep_city_name = None
        self._dep_terminal = None
        self._dep_time = None
        self._flight_no = None
        self._meal = None
        self._plane_model = None
        self._segment_order = None
        self._stop = None
        self._stop_info_list = None
        self._ticket_info_list = None

    @property
    def ac_code(self):
        return self._ac_code

    @ac_code.setter
    def ac_code(self, value):
        self._ac_code = value
    @property
    def ac_name(self):
        return self._ac_name

    @ac_name.setter
    def ac_name(self, value):
        self._ac_name = value
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
    def arr_terminal(self):
        return self._arr_terminal

    @arr_terminal.setter
    def arr_terminal(self, value):
        self._arr_terminal = value
    @property
    def arr_time(self):
        return self._arr_time

    @arr_time.setter
    def arr_time(self, value):
        self._arr_time = value
    @property
    def cabin_code(self):
        return self._cabin_code

    @cabin_code.setter
    def cabin_code(self, value):
        self._cabin_code = value
    @property
    def cabin_name(self):
        return self._cabin_name

    @cabin_name.setter
    def cabin_name(self, value):
        self._cabin_name = value
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
    def dep_terminal(self):
        return self._dep_terminal

    @dep_terminal.setter
    def dep_terminal(self, value):
        self._dep_terminal = value
    @property
    def dep_time(self):
        return self._dep_time

    @dep_time.setter
    def dep_time(self, value):
        self._dep_time = value
    @property
    def flight_no(self):
        return self._flight_no

    @flight_no.setter
    def flight_no(self, value):
        self._flight_no = value
    @property
    def meal(self):
        return self._meal

    @meal.setter
    def meal(self, value):
        self._meal = value
    @property
    def plane_model(self):
        return self._plane_model

    @plane_model.setter
    def plane_model(self, value):
        self._plane_model = value
    @property
    def segment_order(self):
        return self._segment_order

    @segment_order.setter
    def segment_order(self, value):
        self._segment_order = value
    @property
    def stop(self):
        return self._stop

    @stop.setter
    def stop(self, value):
        self._stop = value
    @property
    def stop_info_list(self):
        return self._stop_info_list

    @stop_info_list.setter
    def stop_info_list(self, value):
        if isinstance(value, list):
            self._stop_info_list = list()
            for i in value:
                if isinstance(i, TrafficAirticketOrderStopInfo):
                    self._stop_info_list.append(i)
                else:
                    self._stop_info_list.append(TrafficAirticketOrderStopInfo.from_alipay_dict(i))
    @property
    def ticket_info_list(self):
        return self._ticket_info_list

    @ticket_info_list.setter
    def ticket_info_list(self, value):
        if isinstance(value, list):
            self._ticket_info_list = list()
            for i in value:
                if isinstance(i, TrafficAirticketOrderTicketInfo):
                    self._ticket_info_list.append(i)
                else:
                    self._ticket_info_list.append(TrafficAirticketOrderTicketInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.ac_code:
            if hasattr(self.ac_code, 'to_alipay_dict'):
                params['ac_code'] = self.ac_code.to_alipay_dict()
            else:
                params['ac_code'] = self.ac_code
        if self.ac_name:
            if hasattr(self.ac_name, 'to_alipay_dict'):
                params['ac_name'] = self.ac_name.to_alipay_dict()
            else:
                params['ac_name'] = self.ac_name
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
        if self.arr_terminal:
            if hasattr(self.arr_terminal, 'to_alipay_dict'):
                params['arr_terminal'] = self.arr_terminal.to_alipay_dict()
            else:
                params['arr_terminal'] = self.arr_terminal
        if self.arr_time:
            if hasattr(self.arr_time, 'to_alipay_dict'):
                params['arr_time'] = self.arr_time.to_alipay_dict()
            else:
                params['arr_time'] = self.arr_time
        if self.cabin_code:
            if hasattr(self.cabin_code, 'to_alipay_dict'):
                params['cabin_code'] = self.cabin_code.to_alipay_dict()
            else:
                params['cabin_code'] = self.cabin_code
        if self.cabin_name:
            if hasattr(self.cabin_name, 'to_alipay_dict'):
                params['cabin_name'] = self.cabin_name.to_alipay_dict()
            else:
                params['cabin_name'] = self.cabin_name
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
        if self.dep_terminal:
            if hasattr(self.dep_terminal, 'to_alipay_dict'):
                params['dep_terminal'] = self.dep_terminal.to_alipay_dict()
            else:
                params['dep_terminal'] = self.dep_terminal
        if self.dep_time:
            if hasattr(self.dep_time, 'to_alipay_dict'):
                params['dep_time'] = self.dep_time.to_alipay_dict()
            else:
                params['dep_time'] = self.dep_time
        if self.flight_no:
            if hasattr(self.flight_no, 'to_alipay_dict'):
                params['flight_no'] = self.flight_no.to_alipay_dict()
            else:
                params['flight_no'] = self.flight_no
        if self.meal:
            if hasattr(self.meal, 'to_alipay_dict'):
                params['meal'] = self.meal.to_alipay_dict()
            else:
                params['meal'] = self.meal
        if self.plane_model:
            if hasattr(self.plane_model, 'to_alipay_dict'):
                params['plane_model'] = self.plane_model.to_alipay_dict()
            else:
                params['plane_model'] = self.plane_model
        if self.segment_order:
            if hasattr(self.segment_order, 'to_alipay_dict'):
                params['segment_order'] = self.segment_order.to_alipay_dict()
            else:
                params['segment_order'] = self.segment_order
        if self.stop:
            if hasattr(self.stop, 'to_alipay_dict'):
                params['stop'] = self.stop.to_alipay_dict()
            else:
                params['stop'] = self.stop
        if self.stop_info_list:
            if isinstance(self.stop_info_list, list):
                for i in range(0, len(self.stop_info_list)):
                    element = self.stop_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.stop_info_list[i] = element.to_alipay_dict()
            if hasattr(self.stop_info_list, 'to_alipay_dict'):
                params['stop_info_list'] = self.stop_info_list.to_alipay_dict()
            else:
                params['stop_info_list'] = self.stop_info_list
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
        o = TrafficAirticketOrderSegmentInfo()
        if 'ac_code' in d:
            o.ac_code = d['ac_code']
        if 'ac_name' in d:
            o.ac_name = d['ac_name']
        if 'arr_airport_code' in d:
            o.arr_airport_code = d['arr_airport_code']
        if 'arr_airport_name' in d:
            o.arr_airport_name = d['arr_airport_name']
        if 'arr_city_code' in d:
            o.arr_city_code = d['arr_city_code']
        if 'arr_city_name' in d:
            o.arr_city_name = d['arr_city_name']
        if 'arr_terminal' in d:
            o.arr_terminal = d['arr_terminal']
        if 'arr_time' in d:
            o.arr_time = d['arr_time']
        if 'cabin_code' in d:
            o.cabin_code = d['cabin_code']
        if 'cabin_name' in d:
            o.cabin_name = d['cabin_name']
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
        if 'dep_terminal' in d:
            o.dep_terminal = d['dep_terminal']
        if 'dep_time' in d:
            o.dep_time = d['dep_time']
        if 'flight_no' in d:
            o.flight_no = d['flight_no']
        if 'meal' in d:
            o.meal = d['meal']
        if 'plane_model' in d:
            o.plane_model = d['plane_model']
        if 'segment_order' in d:
            o.segment_order = d['segment_order']
        if 'stop' in d:
            o.stop = d['stop']
        if 'stop_info_list' in d:
            o.stop_info_list = d['stop_info_list']
        if 'ticket_info_list' in d:
            o.ticket_info_list = d['ticket_info_list']
        return o



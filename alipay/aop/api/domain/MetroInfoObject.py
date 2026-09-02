#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AdjustOperationOrganizationObject import AdjustOperationOrganizationObject
from alipay.aop.api.domain.AdjustRouteDirectionObject import AdjustRouteDirectionObject
from alipay.aop.api.domain.BusTransferObject import BusTransferObject
from alipay.aop.api.domain.EffectBusRouteObject import EffectBusRouteObject
from alipay.aop.api.domain.EffectBusStationObject import EffectBusStationObject
from alipay.aop.api.domain.EntranceExitObject import EntranceExitObject
from alipay.aop.api.domain.ParallelRouteObject import ParallelRouteObject
from alipay.aop.api.domain.PassengerFlowPredictObject import PassengerFlowPredictObject
from alipay.aop.api.domain.StationObject import StationObject


class MetroInfoObject(object):

    def __init__(self):
        self._adjust_operation_organization_list = None
        self._adjust_route_direction_list = None
        self._adjustment_suggestions_summary = None
        self._bus_transfer_list = None
        self._bus_transfer_platform_summary = None
        self._down_direction = None
        self._down_time = None
        self._effect_bus_route_list = None
        self._effect_bus_route_summary = None
        self._effect_bus_station_list = None
        self._entrance_exit_list = None
        self._metro_code = None
        self._metro_length = None
        self._metro_name = None
        self._metro_station_count = None
        self._metro_status = None
        self._metro_transfer_route_count = None
        self._metro_transfer_route_detail = None
        self._metro_transfer_station_count = None
        self._metro_transfer_station_detail = None
        self._parallel_bus_route_list = None
        self._parallel_bus_route_summary = None
        self._passenger_flow_predict_list = None
        self._passenger_flow_predict_summary = None
        self._station_list = None
        self._up_direction = None
        self._up_time = None

    @property
    def adjust_operation_organization_list(self):
        return self._adjust_operation_organization_list

    @adjust_operation_organization_list.setter
    def adjust_operation_organization_list(self, value):
        if isinstance(value, list):
            self._adjust_operation_organization_list = list()
            for i in value:
                if isinstance(i, AdjustOperationOrganizationObject):
                    self._adjust_operation_organization_list.append(i)
                else:
                    self._adjust_operation_organization_list.append(AdjustOperationOrganizationObject.from_alipay_dict(i))
    @property
    def adjust_route_direction_list(self):
        return self._adjust_route_direction_list

    @adjust_route_direction_list.setter
    def adjust_route_direction_list(self, value):
        if isinstance(value, list):
            self._adjust_route_direction_list = list()
            for i in value:
                if isinstance(i, AdjustRouteDirectionObject):
                    self._adjust_route_direction_list.append(i)
                else:
                    self._adjust_route_direction_list.append(AdjustRouteDirectionObject.from_alipay_dict(i))
    @property
    def adjustment_suggestions_summary(self):
        return self._adjustment_suggestions_summary

    @adjustment_suggestions_summary.setter
    def adjustment_suggestions_summary(self, value):
        self._adjustment_suggestions_summary = value
    @property
    def bus_transfer_list(self):
        return self._bus_transfer_list

    @bus_transfer_list.setter
    def bus_transfer_list(self, value):
        if isinstance(value, list):
            self._bus_transfer_list = list()
            for i in value:
                if isinstance(i, BusTransferObject):
                    self._bus_transfer_list.append(i)
                else:
                    self._bus_transfer_list.append(BusTransferObject.from_alipay_dict(i))
    @property
    def bus_transfer_platform_summary(self):
        return self._bus_transfer_platform_summary

    @bus_transfer_platform_summary.setter
    def bus_transfer_platform_summary(self, value):
        self._bus_transfer_platform_summary = value
    @property
    def down_direction(self):
        return self._down_direction

    @down_direction.setter
    def down_direction(self, value):
        self._down_direction = value
    @property
    def down_time(self):
        return self._down_time

    @down_time.setter
    def down_time(self, value):
        self._down_time = value
    @property
    def effect_bus_route_list(self):
        return self._effect_bus_route_list

    @effect_bus_route_list.setter
    def effect_bus_route_list(self, value):
        if isinstance(value, list):
            self._effect_bus_route_list = list()
            for i in value:
                if isinstance(i, EffectBusRouteObject):
                    self._effect_bus_route_list.append(i)
                else:
                    self._effect_bus_route_list.append(EffectBusRouteObject.from_alipay_dict(i))
    @property
    def effect_bus_route_summary(self):
        return self._effect_bus_route_summary

    @effect_bus_route_summary.setter
    def effect_bus_route_summary(self, value):
        self._effect_bus_route_summary = value
    @property
    def effect_bus_station_list(self):
        return self._effect_bus_station_list

    @effect_bus_station_list.setter
    def effect_bus_station_list(self, value):
        if isinstance(value, list):
            self._effect_bus_station_list = list()
            for i in value:
                if isinstance(i, EffectBusStationObject):
                    self._effect_bus_station_list.append(i)
                else:
                    self._effect_bus_station_list.append(EffectBusStationObject.from_alipay_dict(i))
    @property
    def entrance_exit_list(self):
        return self._entrance_exit_list

    @entrance_exit_list.setter
    def entrance_exit_list(self, value):
        if isinstance(value, list):
            self._entrance_exit_list = list()
            for i in value:
                if isinstance(i, EntranceExitObject):
                    self._entrance_exit_list.append(i)
                else:
                    self._entrance_exit_list.append(EntranceExitObject.from_alipay_dict(i))
    @property
    def metro_code(self):
        return self._metro_code

    @metro_code.setter
    def metro_code(self, value):
        self._metro_code = value
    @property
    def metro_length(self):
        return self._metro_length

    @metro_length.setter
    def metro_length(self, value):
        self._metro_length = value
    @property
    def metro_name(self):
        return self._metro_name

    @metro_name.setter
    def metro_name(self, value):
        self._metro_name = value
    @property
    def metro_station_count(self):
        return self._metro_station_count

    @metro_station_count.setter
    def metro_station_count(self, value):
        self._metro_station_count = value
    @property
    def metro_status(self):
        return self._metro_status

    @metro_status.setter
    def metro_status(self, value):
        self._metro_status = value
    @property
    def metro_transfer_route_count(self):
        return self._metro_transfer_route_count

    @metro_transfer_route_count.setter
    def metro_transfer_route_count(self, value):
        self._metro_transfer_route_count = value
    @property
    def metro_transfer_route_detail(self):
        return self._metro_transfer_route_detail

    @metro_transfer_route_detail.setter
    def metro_transfer_route_detail(self, value):
        self._metro_transfer_route_detail = value
    @property
    def metro_transfer_station_count(self):
        return self._metro_transfer_station_count

    @metro_transfer_station_count.setter
    def metro_transfer_station_count(self, value):
        self._metro_transfer_station_count = value
    @property
    def metro_transfer_station_detail(self):
        return self._metro_transfer_station_detail

    @metro_transfer_station_detail.setter
    def metro_transfer_station_detail(self, value):
        self._metro_transfer_station_detail = value
    @property
    def parallel_bus_route_list(self):
        return self._parallel_bus_route_list

    @parallel_bus_route_list.setter
    def parallel_bus_route_list(self, value):
        if isinstance(value, list):
            self._parallel_bus_route_list = list()
            for i in value:
                if isinstance(i, ParallelRouteObject):
                    self._parallel_bus_route_list.append(i)
                else:
                    self._parallel_bus_route_list.append(ParallelRouteObject.from_alipay_dict(i))
    @property
    def parallel_bus_route_summary(self):
        return self._parallel_bus_route_summary

    @parallel_bus_route_summary.setter
    def parallel_bus_route_summary(self, value):
        self._parallel_bus_route_summary = value
    @property
    def passenger_flow_predict_list(self):
        return self._passenger_flow_predict_list

    @passenger_flow_predict_list.setter
    def passenger_flow_predict_list(self, value):
        if isinstance(value, list):
            self._passenger_flow_predict_list = list()
            for i in value:
                if isinstance(i, PassengerFlowPredictObject):
                    self._passenger_flow_predict_list.append(i)
                else:
                    self._passenger_flow_predict_list.append(PassengerFlowPredictObject.from_alipay_dict(i))
    @property
    def passenger_flow_predict_summary(self):
        return self._passenger_flow_predict_summary

    @passenger_flow_predict_summary.setter
    def passenger_flow_predict_summary(self, value):
        self._passenger_flow_predict_summary = value
    @property
    def station_list(self):
        return self._station_list

    @station_list.setter
    def station_list(self, value):
        if isinstance(value, list):
            self._station_list = list()
            for i in value:
                if isinstance(i, StationObject):
                    self._station_list.append(i)
                else:
                    self._station_list.append(StationObject.from_alipay_dict(i))
    @property
    def up_direction(self):
        return self._up_direction

    @up_direction.setter
    def up_direction(self, value):
        self._up_direction = value
    @property
    def up_time(self):
        return self._up_time

    @up_time.setter
    def up_time(self, value):
        self._up_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.adjust_operation_organization_list:
            if isinstance(self.adjust_operation_organization_list, list):
                for i in range(0, len(self.adjust_operation_organization_list)):
                    element = self.adjust_operation_organization_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.adjust_operation_organization_list[i] = element.to_alipay_dict()
            if hasattr(self.adjust_operation_organization_list, 'to_alipay_dict'):
                params['adjust_operation_organization_list'] = self.adjust_operation_organization_list.to_alipay_dict()
            else:
                params['adjust_operation_organization_list'] = self.adjust_operation_organization_list
        if self.adjust_route_direction_list:
            if isinstance(self.adjust_route_direction_list, list):
                for i in range(0, len(self.adjust_route_direction_list)):
                    element = self.adjust_route_direction_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.adjust_route_direction_list[i] = element.to_alipay_dict()
            if hasattr(self.adjust_route_direction_list, 'to_alipay_dict'):
                params['adjust_route_direction_list'] = self.adjust_route_direction_list.to_alipay_dict()
            else:
                params['adjust_route_direction_list'] = self.adjust_route_direction_list
        if self.adjustment_suggestions_summary:
            if hasattr(self.adjustment_suggestions_summary, 'to_alipay_dict'):
                params['adjustment_suggestions_summary'] = self.adjustment_suggestions_summary.to_alipay_dict()
            else:
                params['adjustment_suggestions_summary'] = self.adjustment_suggestions_summary
        if self.bus_transfer_list:
            if isinstance(self.bus_transfer_list, list):
                for i in range(0, len(self.bus_transfer_list)):
                    element = self.bus_transfer_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bus_transfer_list[i] = element.to_alipay_dict()
            if hasattr(self.bus_transfer_list, 'to_alipay_dict'):
                params['bus_transfer_list'] = self.bus_transfer_list.to_alipay_dict()
            else:
                params['bus_transfer_list'] = self.bus_transfer_list
        if self.bus_transfer_platform_summary:
            if hasattr(self.bus_transfer_platform_summary, 'to_alipay_dict'):
                params['bus_transfer_platform_summary'] = self.bus_transfer_platform_summary.to_alipay_dict()
            else:
                params['bus_transfer_platform_summary'] = self.bus_transfer_platform_summary
        if self.down_direction:
            if hasattr(self.down_direction, 'to_alipay_dict'):
                params['down_direction'] = self.down_direction.to_alipay_dict()
            else:
                params['down_direction'] = self.down_direction
        if self.down_time:
            if hasattr(self.down_time, 'to_alipay_dict'):
                params['down_time'] = self.down_time.to_alipay_dict()
            else:
                params['down_time'] = self.down_time
        if self.effect_bus_route_list:
            if isinstance(self.effect_bus_route_list, list):
                for i in range(0, len(self.effect_bus_route_list)):
                    element = self.effect_bus_route_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.effect_bus_route_list[i] = element.to_alipay_dict()
            if hasattr(self.effect_bus_route_list, 'to_alipay_dict'):
                params['effect_bus_route_list'] = self.effect_bus_route_list.to_alipay_dict()
            else:
                params['effect_bus_route_list'] = self.effect_bus_route_list
        if self.effect_bus_route_summary:
            if hasattr(self.effect_bus_route_summary, 'to_alipay_dict'):
                params['effect_bus_route_summary'] = self.effect_bus_route_summary.to_alipay_dict()
            else:
                params['effect_bus_route_summary'] = self.effect_bus_route_summary
        if self.effect_bus_station_list:
            if isinstance(self.effect_bus_station_list, list):
                for i in range(0, len(self.effect_bus_station_list)):
                    element = self.effect_bus_station_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.effect_bus_station_list[i] = element.to_alipay_dict()
            if hasattr(self.effect_bus_station_list, 'to_alipay_dict'):
                params['effect_bus_station_list'] = self.effect_bus_station_list.to_alipay_dict()
            else:
                params['effect_bus_station_list'] = self.effect_bus_station_list
        if self.entrance_exit_list:
            if isinstance(self.entrance_exit_list, list):
                for i in range(0, len(self.entrance_exit_list)):
                    element = self.entrance_exit_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.entrance_exit_list[i] = element.to_alipay_dict()
            if hasattr(self.entrance_exit_list, 'to_alipay_dict'):
                params['entrance_exit_list'] = self.entrance_exit_list.to_alipay_dict()
            else:
                params['entrance_exit_list'] = self.entrance_exit_list
        if self.metro_code:
            if hasattr(self.metro_code, 'to_alipay_dict'):
                params['metro_code'] = self.metro_code.to_alipay_dict()
            else:
                params['metro_code'] = self.metro_code
        if self.metro_length:
            if hasattr(self.metro_length, 'to_alipay_dict'):
                params['metro_length'] = self.metro_length.to_alipay_dict()
            else:
                params['metro_length'] = self.metro_length
        if self.metro_name:
            if hasattr(self.metro_name, 'to_alipay_dict'):
                params['metro_name'] = self.metro_name.to_alipay_dict()
            else:
                params['metro_name'] = self.metro_name
        if self.metro_station_count:
            if hasattr(self.metro_station_count, 'to_alipay_dict'):
                params['metro_station_count'] = self.metro_station_count.to_alipay_dict()
            else:
                params['metro_station_count'] = self.metro_station_count
        if self.metro_status:
            if hasattr(self.metro_status, 'to_alipay_dict'):
                params['metro_status'] = self.metro_status.to_alipay_dict()
            else:
                params['metro_status'] = self.metro_status
        if self.metro_transfer_route_count:
            if hasattr(self.metro_transfer_route_count, 'to_alipay_dict'):
                params['metro_transfer_route_count'] = self.metro_transfer_route_count.to_alipay_dict()
            else:
                params['metro_transfer_route_count'] = self.metro_transfer_route_count
        if self.metro_transfer_route_detail:
            if hasattr(self.metro_transfer_route_detail, 'to_alipay_dict'):
                params['metro_transfer_route_detail'] = self.metro_transfer_route_detail.to_alipay_dict()
            else:
                params['metro_transfer_route_detail'] = self.metro_transfer_route_detail
        if self.metro_transfer_station_count:
            if hasattr(self.metro_transfer_station_count, 'to_alipay_dict'):
                params['metro_transfer_station_count'] = self.metro_transfer_station_count.to_alipay_dict()
            else:
                params['metro_transfer_station_count'] = self.metro_transfer_station_count
        if self.metro_transfer_station_detail:
            if hasattr(self.metro_transfer_station_detail, 'to_alipay_dict'):
                params['metro_transfer_station_detail'] = self.metro_transfer_station_detail.to_alipay_dict()
            else:
                params['metro_transfer_station_detail'] = self.metro_transfer_station_detail
        if self.parallel_bus_route_list:
            if isinstance(self.parallel_bus_route_list, list):
                for i in range(0, len(self.parallel_bus_route_list)):
                    element = self.parallel_bus_route_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.parallel_bus_route_list[i] = element.to_alipay_dict()
            if hasattr(self.parallel_bus_route_list, 'to_alipay_dict'):
                params['parallel_bus_route_list'] = self.parallel_bus_route_list.to_alipay_dict()
            else:
                params['parallel_bus_route_list'] = self.parallel_bus_route_list
        if self.parallel_bus_route_summary:
            if hasattr(self.parallel_bus_route_summary, 'to_alipay_dict'):
                params['parallel_bus_route_summary'] = self.parallel_bus_route_summary.to_alipay_dict()
            else:
                params['parallel_bus_route_summary'] = self.parallel_bus_route_summary
        if self.passenger_flow_predict_list:
            if isinstance(self.passenger_flow_predict_list, list):
                for i in range(0, len(self.passenger_flow_predict_list)):
                    element = self.passenger_flow_predict_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.passenger_flow_predict_list[i] = element.to_alipay_dict()
            if hasattr(self.passenger_flow_predict_list, 'to_alipay_dict'):
                params['passenger_flow_predict_list'] = self.passenger_flow_predict_list.to_alipay_dict()
            else:
                params['passenger_flow_predict_list'] = self.passenger_flow_predict_list
        if self.passenger_flow_predict_summary:
            if hasattr(self.passenger_flow_predict_summary, 'to_alipay_dict'):
                params['passenger_flow_predict_summary'] = self.passenger_flow_predict_summary.to_alipay_dict()
            else:
                params['passenger_flow_predict_summary'] = self.passenger_flow_predict_summary
        if self.station_list:
            if isinstance(self.station_list, list):
                for i in range(0, len(self.station_list)):
                    element = self.station_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.station_list[i] = element.to_alipay_dict()
            if hasattr(self.station_list, 'to_alipay_dict'):
                params['station_list'] = self.station_list.to_alipay_dict()
            else:
                params['station_list'] = self.station_list
        if self.up_direction:
            if hasattr(self.up_direction, 'to_alipay_dict'):
                params['up_direction'] = self.up_direction.to_alipay_dict()
            else:
                params['up_direction'] = self.up_direction
        if self.up_time:
            if hasattr(self.up_time, 'to_alipay_dict'):
                params['up_time'] = self.up_time.to_alipay_dict()
            else:
                params['up_time'] = self.up_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MetroInfoObject()
        if 'adjust_operation_organization_list' in d:
            o.adjust_operation_organization_list = d['adjust_operation_organization_list']
        if 'adjust_route_direction_list' in d:
            o.adjust_route_direction_list = d['adjust_route_direction_list']
        if 'adjustment_suggestions_summary' in d:
            o.adjustment_suggestions_summary = d['adjustment_suggestions_summary']
        if 'bus_transfer_list' in d:
            o.bus_transfer_list = d['bus_transfer_list']
        if 'bus_transfer_platform_summary' in d:
            o.bus_transfer_platform_summary = d['bus_transfer_platform_summary']
        if 'down_direction' in d:
            o.down_direction = d['down_direction']
        if 'down_time' in d:
            o.down_time = d['down_time']
        if 'effect_bus_route_list' in d:
            o.effect_bus_route_list = d['effect_bus_route_list']
        if 'effect_bus_route_summary' in d:
            o.effect_bus_route_summary = d['effect_bus_route_summary']
        if 'effect_bus_station_list' in d:
            o.effect_bus_station_list = d['effect_bus_station_list']
        if 'entrance_exit_list' in d:
            o.entrance_exit_list = d['entrance_exit_list']
        if 'metro_code' in d:
            o.metro_code = d['metro_code']
        if 'metro_length' in d:
            o.metro_length = d['metro_length']
        if 'metro_name' in d:
            o.metro_name = d['metro_name']
        if 'metro_station_count' in d:
            o.metro_station_count = d['metro_station_count']
        if 'metro_status' in d:
            o.metro_status = d['metro_status']
        if 'metro_transfer_route_count' in d:
            o.metro_transfer_route_count = d['metro_transfer_route_count']
        if 'metro_transfer_route_detail' in d:
            o.metro_transfer_route_detail = d['metro_transfer_route_detail']
        if 'metro_transfer_station_count' in d:
            o.metro_transfer_station_count = d['metro_transfer_station_count']
        if 'metro_transfer_station_detail' in d:
            o.metro_transfer_station_detail = d['metro_transfer_station_detail']
        if 'parallel_bus_route_list' in d:
            o.parallel_bus_route_list = d['parallel_bus_route_list']
        if 'parallel_bus_route_summary' in d:
            o.parallel_bus_route_summary = d['parallel_bus_route_summary']
        if 'passenger_flow_predict_list' in d:
            o.passenger_flow_predict_list = d['passenger_flow_predict_list']
        if 'passenger_flow_predict_summary' in d:
            o.passenger_flow_predict_summary = d['passenger_flow_predict_summary']
        if 'station_list' in d:
            o.station_list = d['station_list']
        if 'up_direction' in d:
            o.up_direction = d['up_direction']
        if 'up_time' in d:
            o.up_time = d['up_time']
        return o



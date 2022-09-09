#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.HotelRoomFaceInfoRes import HotelRoomFaceInfoRes


class AlipayOpenIotmbsHoteldeviceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenIotmbsHoteldeviceQueryResponse, self).__init__()
        self._face_list = None
        self._function_list = None
        self._group_id = None
        self._hotel_name = None
        self._poll_time = None
        self._room_no = None
        self._room_status = None

    @property
    def face_list(self):
        return self._face_list

    @face_list.setter
    def face_list(self, value):
        if isinstance(value, list):
            self._face_list = list()
            for i in value:
                if isinstance(i, HotelRoomFaceInfoRes):
                    self._face_list.append(i)
                else:
                    self._face_list.append(HotelRoomFaceInfoRes.from_alipay_dict(i))
    @property
    def function_list(self):
        return self._function_list

    @function_list.setter
    def function_list(self, value):
        if isinstance(value, list):
            self._function_list = list()
            for i in value:
                self._function_list.append(i)
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def hotel_name(self):
        return self._hotel_name

    @hotel_name.setter
    def hotel_name(self, value):
        self._hotel_name = value
    @property
    def poll_time(self):
        return self._poll_time

    @poll_time.setter
    def poll_time(self, value):
        self._poll_time = value
    @property
    def room_no(self):
        return self._room_no

    @room_no.setter
    def room_no(self, value):
        self._room_no = value
    @property
    def room_status(self):
        return self._room_status

    @room_status.setter
    def room_status(self, value):
        self._room_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenIotmbsHoteldeviceQueryResponse, self).parse_response_content(response_content)
        if 'face_list' in response:
            self.face_list = response['face_list']
        if 'function_list' in response:
            self.function_list = response['function_list']
        if 'group_id' in response:
            self.group_id = response['group_id']
        if 'hotel_name' in response:
            self.hotel_name = response['hotel_name']
        if 'poll_time' in response:
            self.poll_time = response['poll_time']
        if 'room_no' in response:
            self.room_no = response['room_no']
        if 'room_status' in response:
            self.room_status = response['room_status']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BreakCostsInfo import BreakCostsInfo
from alipay.aop.api.domain.CardPromoInfo import CardPromoInfo
from alipay.aop.api.domain.AxfItemAttr import AxfItemAttr
from alipay.aop.api.domain.MoneyCardInfo import MoneyCardInfo
from alipay.aop.api.domain.CardRejectReasonInfo import CardRejectReasonInfo
from alipay.aop.api.domain.CardTemplateSale import CardTemplateSale
from alipay.aop.api.domain.TimesCardInfo import TimesCardInfo
from alipay.aop.api.domain.CardTemplateUse import CardTemplateUse


class MerchantCardTemplate(object):

    def __init__(self):
        self._ax_item_type = None
        self._booking_cancel_deadline = None
        self._booking_mode = None
        self._break_costs_info = None
        self._card_promo_list = None
        self._card_template_app_id = None
        self._card_template_id = None
        self._card_template_name = None
        self._card_template_status = None
        self._card_type = None
        self._category_id = None
        self._funding_model = None
        self._hotline = None
        self._image_detail_id_list = None
        self._image_detail_url_list = None
        self._image_id_list = None
        self._image_url_list = None
        self._item_attrs = None
        self._item_category_code = None
        self._money_card_info = None
        self._msg_app_id = None
        self._need_order_agreement = None
        self._online_sale_switch = None
        self._online_show_switch = None
        self._out_card_id = None
        self._reject_reasons = None
        self._sale_info = None
        self._settle_type = None
        self._support_withdraw = None
        self._times_card_info = None
        self._use_info = None

    @property
    def ax_item_type(self):
        return self._ax_item_type

    @ax_item_type.setter
    def ax_item_type(self, value):
        self._ax_item_type = value
    @property
    def booking_cancel_deadline(self):
        return self._booking_cancel_deadline

    @booking_cancel_deadline.setter
    def booking_cancel_deadline(self, value):
        self._booking_cancel_deadline = value
    @property
    def booking_mode(self):
        return self._booking_mode

    @booking_mode.setter
    def booking_mode(self, value):
        self._booking_mode = value
    @property
    def break_costs_info(self):
        return self._break_costs_info

    @break_costs_info.setter
    def break_costs_info(self, value):
        if isinstance(value, BreakCostsInfo):
            self._break_costs_info = value
        else:
            self._break_costs_info = BreakCostsInfo.from_alipay_dict(value)
    @property
    def card_promo_list(self):
        return self._card_promo_list

    @card_promo_list.setter
    def card_promo_list(self, value):
        if isinstance(value, list):
            self._card_promo_list = list()
            for i in value:
                if isinstance(i, CardPromoInfo):
                    self._card_promo_list.append(i)
                else:
                    self._card_promo_list.append(CardPromoInfo.from_alipay_dict(i))
    @property
    def card_template_app_id(self):
        return self._card_template_app_id

    @card_template_app_id.setter
    def card_template_app_id(self, value):
        self._card_template_app_id = value
    @property
    def card_template_id(self):
        return self._card_template_id

    @card_template_id.setter
    def card_template_id(self, value):
        self._card_template_id = value
    @property
    def card_template_name(self):
        return self._card_template_name

    @card_template_name.setter
    def card_template_name(self, value):
        self._card_template_name = value
    @property
    def card_template_status(self):
        return self._card_template_status

    @card_template_status.setter
    def card_template_status(self, value):
        self._card_template_status = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def funding_model(self):
        return self._funding_model

    @funding_model.setter
    def funding_model(self, value):
        if isinstance(value, list):
            self._funding_model = list()
            for i in value:
                self._funding_model.append(i)
    @property
    def hotline(self):
        return self._hotline

    @hotline.setter
    def hotline(self, value):
        self._hotline = value
    @property
    def image_detail_id_list(self):
        return self._image_detail_id_list

    @image_detail_id_list.setter
    def image_detail_id_list(self, value):
        if isinstance(value, list):
            self._image_detail_id_list = list()
            for i in value:
                self._image_detail_id_list.append(i)
    @property
    def image_detail_url_list(self):
        return self._image_detail_url_list

    @image_detail_url_list.setter
    def image_detail_url_list(self, value):
        if isinstance(value, list):
            self._image_detail_url_list = list()
            for i in value:
                self._image_detail_url_list.append(i)
    @property
    def image_id_list(self):
        return self._image_id_list

    @image_id_list.setter
    def image_id_list(self, value):
        if isinstance(value, list):
            self._image_id_list = list()
            for i in value:
                self._image_id_list.append(i)
    @property
    def image_url_list(self):
        return self._image_url_list

    @image_url_list.setter
    def image_url_list(self, value):
        if isinstance(value, list):
            self._image_url_list = list()
            for i in value:
                self._image_url_list.append(i)
    @property
    def item_attrs(self):
        return self._item_attrs

    @item_attrs.setter
    def item_attrs(self, value):
        if isinstance(value, list):
            self._item_attrs = list()
            for i in value:
                if isinstance(i, AxfItemAttr):
                    self._item_attrs.append(i)
                else:
                    self._item_attrs.append(AxfItemAttr.from_alipay_dict(i))
    @property
    def item_category_code(self):
        return self._item_category_code

    @item_category_code.setter
    def item_category_code(self, value):
        self._item_category_code = value
    @property
    def money_card_info(self):
        return self._money_card_info

    @money_card_info.setter
    def money_card_info(self, value):
        if isinstance(value, MoneyCardInfo):
            self._money_card_info = value
        else:
            self._money_card_info = MoneyCardInfo.from_alipay_dict(value)
    @property
    def msg_app_id(self):
        return self._msg_app_id

    @msg_app_id.setter
    def msg_app_id(self, value):
        self._msg_app_id = value
    @property
    def need_order_agreement(self):
        return self._need_order_agreement

    @need_order_agreement.setter
    def need_order_agreement(self, value):
        self._need_order_agreement = value
    @property
    def online_sale_switch(self):
        return self._online_sale_switch

    @online_sale_switch.setter
    def online_sale_switch(self, value):
        self._online_sale_switch = value
    @property
    def online_show_switch(self):
        return self._online_show_switch

    @online_show_switch.setter
    def online_show_switch(self, value):
        self._online_show_switch = value
    @property
    def out_card_id(self):
        return self._out_card_id

    @out_card_id.setter
    def out_card_id(self, value):
        self._out_card_id = value
    @property
    def reject_reasons(self):
        return self._reject_reasons

    @reject_reasons.setter
    def reject_reasons(self, value):
        if isinstance(value, list):
            self._reject_reasons = list()
            for i in value:
                if isinstance(i, CardRejectReasonInfo):
                    self._reject_reasons.append(i)
                else:
                    self._reject_reasons.append(CardRejectReasonInfo.from_alipay_dict(i))
    @property
    def sale_info(self):
        return self._sale_info

    @sale_info.setter
    def sale_info(self, value):
        if isinstance(value, CardTemplateSale):
            self._sale_info = value
        else:
            self._sale_info = CardTemplateSale.from_alipay_dict(value)
    @property
    def settle_type(self):
        return self._settle_type

    @settle_type.setter
    def settle_type(self, value):
        self._settle_type = value
    @property
    def support_withdraw(self):
        return self._support_withdraw

    @support_withdraw.setter
    def support_withdraw(self, value):
        self._support_withdraw = value
    @property
    def times_card_info(self):
        return self._times_card_info

    @times_card_info.setter
    def times_card_info(self, value):
        if isinstance(value, TimesCardInfo):
            self._times_card_info = value
        else:
            self._times_card_info = TimesCardInfo.from_alipay_dict(value)
    @property
    def use_info(self):
        return self._use_info

    @use_info.setter
    def use_info(self, value):
        if isinstance(value, CardTemplateUse):
            self._use_info = value
        else:
            self._use_info = CardTemplateUse.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.ax_item_type:
            if hasattr(self.ax_item_type, 'to_alipay_dict'):
                params['ax_item_type'] = self.ax_item_type.to_alipay_dict()
            else:
                params['ax_item_type'] = self.ax_item_type
        if self.booking_cancel_deadline:
            if hasattr(self.booking_cancel_deadline, 'to_alipay_dict'):
                params['booking_cancel_deadline'] = self.booking_cancel_deadline.to_alipay_dict()
            else:
                params['booking_cancel_deadline'] = self.booking_cancel_deadline
        if self.booking_mode:
            if hasattr(self.booking_mode, 'to_alipay_dict'):
                params['booking_mode'] = self.booking_mode.to_alipay_dict()
            else:
                params['booking_mode'] = self.booking_mode
        if self.break_costs_info:
            if hasattr(self.break_costs_info, 'to_alipay_dict'):
                params['break_costs_info'] = self.break_costs_info.to_alipay_dict()
            else:
                params['break_costs_info'] = self.break_costs_info
        if self.card_promo_list:
            if isinstance(self.card_promo_list, list):
                for i in range(0, len(self.card_promo_list)):
                    element = self.card_promo_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.card_promo_list[i] = element.to_alipay_dict()
            if hasattr(self.card_promo_list, 'to_alipay_dict'):
                params['card_promo_list'] = self.card_promo_list.to_alipay_dict()
            else:
                params['card_promo_list'] = self.card_promo_list
        if self.card_template_app_id:
            if hasattr(self.card_template_app_id, 'to_alipay_dict'):
                params['card_template_app_id'] = self.card_template_app_id.to_alipay_dict()
            else:
                params['card_template_app_id'] = self.card_template_app_id
        if self.card_template_id:
            if hasattr(self.card_template_id, 'to_alipay_dict'):
                params['card_template_id'] = self.card_template_id.to_alipay_dict()
            else:
                params['card_template_id'] = self.card_template_id
        if self.card_template_name:
            if hasattr(self.card_template_name, 'to_alipay_dict'):
                params['card_template_name'] = self.card_template_name.to_alipay_dict()
            else:
                params['card_template_name'] = self.card_template_name
        if self.card_template_status:
            if hasattr(self.card_template_status, 'to_alipay_dict'):
                params['card_template_status'] = self.card_template_status.to_alipay_dict()
            else:
                params['card_template_status'] = self.card_template_status
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.funding_model:
            if isinstance(self.funding_model, list):
                for i in range(0, len(self.funding_model)):
                    element = self.funding_model[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.funding_model[i] = element.to_alipay_dict()
            if hasattr(self.funding_model, 'to_alipay_dict'):
                params['funding_model'] = self.funding_model.to_alipay_dict()
            else:
                params['funding_model'] = self.funding_model
        if self.hotline:
            if hasattr(self.hotline, 'to_alipay_dict'):
                params['hotline'] = self.hotline.to_alipay_dict()
            else:
                params['hotline'] = self.hotline
        if self.image_detail_id_list:
            if isinstance(self.image_detail_id_list, list):
                for i in range(0, len(self.image_detail_id_list)):
                    element = self.image_detail_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.image_detail_id_list[i] = element.to_alipay_dict()
            if hasattr(self.image_detail_id_list, 'to_alipay_dict'):
                params['image_detail_id_list'] = self.image_detail_id_list.to_alipay_dict()
            else:
                params['image_detail_id_list'] = self.image_detail_id_list
        if self.image_detail_url_list:
            if isinstance(self.image_detail_url_list, list):
                for i in range(0, len(self.image_detail_url_list)):
                    element = self.image_detail_url_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.image_detail_url_list[i] = element.to_alipay_dict()
            if hasattr(self.image_detail_url_list, 'to_alipay_dict'):
                params['image_detail_url_list'] = self.image_detail_url_list.to_alipay_dict()
            else:
                params['image_detail_url_list'] = self.image_detail_url_list
        if self.image_id_list:
            if isinstance(self.image_id_list, list):
                for i in range(0, len(self.image_id_list)):
                    element = self.image_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.image_id_list[i] = element.to_alipay_dict()
            if hasattr(self.image_id_list, 'to_alipay_dict'):
                params['image_id_list'] = self.image_id_list.to_alipay_dict()
            else:
                params['image_id_list'] = self.image_id_list
        if self.image_url_list:
            if isinstance(self.image_url_list, list):
                for i in range(0, len(self.image_url_list)):
                    element = self.image_url_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.image_url_list[i] = element.to_alipay_dict()
            if hasattr(self.image_url_list, 'to_alipay_dict'):
                params['image_url_list'] = self.image_url_list.to_alipay_dict()
            else:
                params['image_url_list'] = self.image_url_list
        if self.item_attrs:
            if isinstance(self.item_attrs, list):
                for i in range(0, len(self.item_attrs)):
                    element = self.item_attrs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_attrs[i] = element.to_alipay_dict()
            if hasattr(self.item_attrs, 'to_alipay_dict'):
                params['item_attrs'] = self.item_attrs.to_alipay_dict()
            else:
                params['item_attrs'] = self.item_attrs
        if self.item_category_code:
            if hasattr(self.item_category_code, 'to_alipay_dict'):
                params['item_category_code'] = self.item_category_code.to_alipay_dict()
            else:
                params['item_category_code'] = self.item_category_code
        if self.money_card_info:
            if hasattr(self.money_card_info, 'to_alipay_dict'):
                params['money_card_info'] = self.money_card_info.to_alipay_dict()
            else:
                params['money_card_info'] = self.money_card_info
        if self.msg_app_id:
            if hasattr(self.msg_app_id, 'to_alipay_dict'):
                params['msg_app_id'] = self.msg_app_id.to_alipay_dict()
            else:
                params['msg_app_id'] = self.msg_app_id
        if self.need_order_agreement:
            if hasattr(self.need_order_agreement, 'to_alipay_dict'):
                params['need_order_agreement'] = self.need_order_agreement.to_alipay_dict()
            else:
                params['need_order_agreement'] = self.need_order_agreement
        if self.online_sale_switch:
            if hasattr(self.online_sale_switch, 'to_alipay_dict'):
                params['online_sale_switch'] = self.online_sale_switch.to_alipay_dict()
            else:
                params['online_sale_switch'] = self.online_sale_switch
        if self.online_show_switch:
            if hasattr(self.online_show_switch, 'to_alipay_dict'):
                params['online_show_switch'] = self.online_show_switch.to_alipay_dict()
            else:
                params['online_show_switch'] = self.online_show_switch
        if self.out_card_id:
            if hasattr(self.out_card_id, 'to_alipay_dict'):
                params['out_card_id'] = self.out_card_id.to_alipay_dict()
            else:
                params['out_card_id'] = self.out_card_id
        if self.reject_reasons:
            if isinstance(self.reject_reasons, list):
                for i in range(0, len(self.reject_reasons)):
                    element = self.reject_reasons[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.reject_reasons[i] = element.to_alipay_dict()
            if hasattr(self.reject_reasons, 'to_alipay_dict'):
                params['reject_reasons'] = self.reject_reasons.to_alipay_dict()
            else:
                params['reject_reasons'] = self.reject_reasons
        if self.sale_info:
            if hasattr(self.sale_info, 'to_alipay_dict'):
                params['sale_info'] = self.sale_info.to_alipay_dict()
            else:
                params['sale_info'] = self.sale_info
        if self.settle_type:
            if hasattr(self.settle_type, 'to_alipay_dict'):
                params['settle_type'] = self.settle_type.to_alipay_dict()
            else:
                params['settle_type'] = self.settle_type
        if self.support_withdraw:
            if hasattr(self.support_withdraw, 'to_alipay_dict'):
                params['support_withdraw'] = self.support_withdraw.to_alipay_dict()
            else:
                params['support_withdraw'] = self.support_withdraw
        if self.times_card_info:
            if hasattr(self.times_card_info, 'to_alipay_dict'):
                params['times_card_info'] = self.times_card_info.to_alipay_dict()
            else:
                params['times_card_info'] = self.times_card_info
        if self.use_info:
            if hasattr(self.use_info, 'to_alipay_dict'):
                params['use_info'] = self.use_info.to_alipay_dict()
            else:
                params['use_info'] = self.use_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantCardTemplate()
        if 'ax_item_type' in d:
            o.ax_item_type = d['ax_item_type']
        if 'booking_cancel_deadline' in d:
            o.booking_cancel_deadline = d['booking_cancel_deadline']
        if 'booking_mode' in d:
            o.booking_mode = d['booking_mode']
        if 'break_costs_info' in d:
            o.break_costs_info = d['break_costs_info']
        if 'card_promo_list' in d:
            o.card_promo_list = d['card_promo_list']
        if 'card_template_app_id' in d:
            o.card_template_app_id = d['card_template_app_id']
        if 'card_template_id' in d:
            o.card_template_id = d['card_template_id']
        if 'card_template_name' in d:
            o.card_template_name = d['card_template_name']
        if 'card_template_status' in d:
            o.card_template_status = d['card_template_status']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'funding_model' in d:
            o.funding_model = d['funding_model']
        if 'hotline' in d:
            o.hotline = d['hotline']
        if 'image_detail_id_list' in d:
            o.image_detail_id_list = d['image_detail_id_list']
        if 'image_detail_url_list' in d:
            o.image_detail_url_list = d['image_detail_url_list']
        if 'image_id_list' in d:
            o.image_id_list = d['image_id_list']
        if 'image_url_list' in d:
            o.image_url_list = d['image_url_list']
        if 'item_attrs' in d:
            o.item_attrs = d['item_attrs']
        if 'item_category_code' in d:
            o.item_category_code = d['item_category_code']
        if 'money_card_info' in d:
            o.money_card_info = d['money_card_info']
        if 'msg_app_id' in d:
            o.msg_app_id = d['msg_app_id']
        if 'need_order_agreement' in d:
            o.need_order_agreement = d['need_order_agreement']
        if 'online_sale_switch' in d:
            o.online_sale_switch = d['online_sale_switch']
        if 'online_show_switch' in d:
            o.online_show_switch = d['online_show_switch']
        if 'out_card_id' in d:
            o.out_card_id = d['out_card_id']
        if 'reject_reasons' in d:
            o.reject_reasons = d['reject_reasons']
        if 'sale_info' in d:
            o.sale_info = d['sale_info']
        if 'settle_type' in d:
            o.settle_type = d['settle_type']
        if 'support_withdraw' in d:
            o.support_withdraw = d['support_withdraw']
        if 'times_card_info' in d:
            o.times_card_info = d['times_card_info']
        if 'use_info' in d:
            o.use_info = d['use_info']
        return o



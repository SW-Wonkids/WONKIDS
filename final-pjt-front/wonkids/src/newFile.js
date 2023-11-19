import { RouterLink, RouterView } from 'vue-router';
import { useCounterStore } from '@/stores/counter';

export default (() => {
const __VLS_setup = async () => {
const __VLS_publicComponent = (await import('vue')).defineComponent({
setup() {
return {};
},
});

const __VLS_componentsOption = {};

let __VLS_name!: 'App';
function __VLS_template() {
let __VLS_ctx!: InstanceType<import('./__VLS_types.js').PickNotAny<typeof __VLS_publicComponent, new () => {}>> & InstanceType<import('./__VLS_types.js').PickNotAny<typeof __VLS_internalComponent, new () => {}>> & {};
/* Components */
let __VLS_localComponents!: NonNullable<typeof __VLS_internalComponent extends { components: infer C; } ? C : {}> & typeof __VLS_componentsOption & typeof __VLS_ctx;
let __VLS_otherComponents!: typeof __VLS_localComponents & import('./__VLS_types.js').GlobalComponents;
let __VLS_own!: import('./__VLS_types.js').SelfComponent<typeof __VLS_name, typeof __VLS_internalComponent & typeof __VLS_publicComponent & (new () => { $slots: typeof __VLS_slots; }) >;
let __VLS_components!: typeof __VLS_otherComponents & Omit<typeof __VLS_own, keyof typeof __VLS_otherComponents>;
/* Style Scoped */
type __VLS_StyleScopedClasses = {} &
{ 'wrapper'?: boolean; };
let __VLS_styleScopedClasses!: __VLS_StyleScopedClasses | keyof __VLS_StyleScopedClasses | (keyof __VLS_StyleScopedClasses)[];
/* CSS variable injection */
/* CSS variable injection end */
let __VLS_templateComponents!: {} &
import('./__VLS_types.js').WithComponent<'RouterLink', typeof __VLS_components, 'RouterLink'> &
import('./__VLS_types.js').WithComponent<'RouterView', typeof __VLS_components, 'RouterView'>;
__VLS_components.RouterLink; __VLS_components.RouterLink; __VLS_components.RouterLink; __VLS_components.RouterLink; __VLS_components.RouterLink; __VLS_components.RouterLink; __VLS_components.RouterLink; __VLS_components.RouterLink; __VLS_components.RouterLink; __VLS_components.RouterLink; __VLS_components.RouterLink; __VLS_components.RouterLink; __VLS_components.RouterLink; __VLS_components.RouterLink; __VLS_components.RouterLink; __VLS_components.RouterLink; __VLS_components.RouterLink; __VLS_components.RouterLink; __VLS_components.RouterLink; __VLS_components.RouterLink; __VLS_components.RouterLink; __VLS_components.RouterLink; __VLS_components.RouterLink; __VLS_components.RouterLink; __VLS_components.RouterLink; __VLS_components.RouterLink;
// @ts-ignore
[RouterLink, RouterLink, RouterLink, RouterLink, RouterLink, RouterLink, RouterLink, RouterLink, RouterLink, RouterLink, RouterLink, RouterLink, RouterLink, RouterLink, RouterLink, RouterLink, RouterLink, RouterLink, RouterLink, RouterLink, RouterLink, RouterLink, RouterLink, RouterLink, RouterLink, RouterLink,];
__VLS_components.RouterView;
// @ts-ignore
[RouterView,];
{
({} as JSX.IntrinsicElements).header;
({} as JSX.IntrinsicElements).header;
(__VLS_x as JSX.IntrinsicElements)['header'] = {};
{
({} as JSX.IntrinsicElements).div;
({} as JSX.IntrinsicElements).div;
(__VLS_x as JSX.IntrinsicElements)['div'] = { class: ("wrapper"), };
if (__VLS_ctx.useCounterStore.isLogin) {
// @ts-ignore
[useCounterStore,];
{
({} as JSX.IntrinsicElements).nav;
({} as JSX.IntrinsicElements).nav;
(__VLS_x as JSX.IntrinsicElements)['nav'] = {};
{
__VLS_templateComponents.RouterLink;
(__VLS_x as import('./__VLS_types.js').ComponentProps<typeof __VLS_templateComponents.RouterLink>) = { to: (({ name: 'home' })), };
}
{
__VLS_templateComponents.RouterLink;
(__VLS_x as import('./__VLS_types.js').ComponentProps<typeof __VLS_templateComponents.RouterLink>) = { to: (({ name: 'logout' })), };
}
{
__VLS_templateComponents.RouterLink;
(__VLS_x as import('./__VLS_types.js').ComponentProps<typeof __VLS_templateComponents.RouterLink>) = { to: (({ name: 'banklist' })), };
}
{
__VLS_templateComponents.RouterLink;
(__VLS_x as import('./__VLS_types.js').ComponentProps<typeof __VLS_templateComponents.RouterLink>) = { to: (({ name: 'profile' })), };
}
{
__VLS_templateComponents.RouterLink;
(__VLS_x as import('./__VLS_types.js').ComponentProps<typeof __VLS_templateComponents.RouterLink>) = { to: (({ name: 'article-list' })), };
}
{
__VLS_templateComponents.RouterLink;
(__VLS_x as import('./__VLS_types.js').ComponentProps<typeof __VLS_templateComponents.RouterLink>) = { to: (({ name: 'poll' })), };
}
}
}
{
({} as JSX.IntrinsicElements).nav;
({} as JSX.IntrinsicElements).nav;
(__VLS_x as JSX.IntrinsicElements)['nav'] = {};
{
__VLS_templateComponents.RouterLink;
(__VLS_x as import('./__VLS_types.js').ComponentProps<typeof __VLS_templateComponents.RouterLink>) = { to: (({ name: 'home' })), };
}
{
__VLS_templateComponents.RouterLink;
(__VLS_x as import('./__VLS_types.js').ComponentProps<typeof __VLS_templateComponents.RouterLink>) = { to: (({ name: 'signup' })), };
}
{
__VLS_templateComponents.RouterLink;
(__VLS_x as import('./__VLS_types.js').ComponentProps<typeof __VLS_templateComponents.RouterLink>) = { to: (({ name: 'login' })), };
}
{
__VLS_templateComponents.RouterLink;
(__VLS_x as import('./__VLS_types.js').ComponentProps<typeof __VLS_templateComponents.RouterLink>) = { to: (({ name: 'banklist' })), };
}
{
__VLS_templateComponents.RouterLink;
(__VLS_x as import('./__VLS_types.js').ComponentProps<typeof __VLS_templateComponents.RouterLink>) = { to: (({ name: 'profile' })), };
}
{
__VLS_templateComponents.RouterLink;
(__VLS_x as import('./__VLS_types.js').ComponentProps<typeof __VLS_templateComponents.RouterLink>) = { to: (({ name: 'article-list' })), };
}
{
__VLS_templateComponents.RouterLink;
(__VLS_x as import('./__VLS_types.js').ComponentProps<typeof __VLS_templateComponents.RouterLink>) = { to: (({ name: 'poll' })), };
}
}
}
}
{
(__VLS_x as import('./__VLS_types.js').ComponentProps<typeof __VLS_templateComponents.RouterView>) = {};
}
if (typeof __VLS_styleScopedClasses === 'object' && !Array.isArray(__VLS_styleScopedClasses)) {
__VLS_styleScopedClasses['wrapper'];
}
declare var __VLS_slots: {};
return __VLS_slots;
}
const __VLS_internalComponent = (await import('vue')).defineComponent({
setup() {
return {
RouterLink: RouterLink,
RouterView: RouterView,
useCounterStore: useCounterStore,
};
},
});
return {} as typeof __VLS_publicComponent;
};
return {} as typeof __VLS_setup extends () => Promise<infer T> ? T : never;
})({} as any);

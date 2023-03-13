import {createRouter, createWebHistory} from 'vue-router'
import HomeView from "@/views/HomeView.vue";
import AuthorizationUser from "@/components/AuthorizationUser.vue";
import MainViews from "@/views/MainViews.vue";
import LoginView from "@/views/LoginView.vue";
import UserPageView from "@/views/UserPageView.vue";
import CreatePostView from "@/views/CreatePostView.vue";
import ShowAllPostViws from "@/views/ShowAllPostViws.vue";
import ShowMyPost from "@/components/ShowMyPost.vue";
import EditPostView from "@/views/EditPostView.vue";


const routes = [
    {
        path: '/',
        name: '',
        component: MainViews,
    },
    {
        path: '/home',
        name: 'Home',
        component: HomeView,
    },
    {
        path: '/Authorization',
        name: 'Authorization',
        component: AuthorizationUser,
    },
    {
        path: '/Login',
        name: 'Login',
        component: LoginView,
        meta: {previousPath: null}
    },
    {
        path: '/UserPage',
        name: 'UserPage',
        component: UserPageView,
        meta: {previousPath: null}
    },
    {
        path: '/CreatePost',
        name: 'CreatePost',
        component: CreatePostView,
    },
    {
        path: '/ShowAllPost',
        name: 'ShowAllPost',
        component: ShowAllPostViws,
        meta: {previousPath: null}
    },
    {
        path: '/ShowMyPost',
        name: 'ShowMyPost',
        component: ShowMyPost,
        meta: {previousPath: null}
    },
    {
        path: '/EditPost/:id',
        name: 'EditPost',
        component: EditPostView,
        meta: {previousPath: null}
    },


]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})
router.beforeEach((to, from, next) => {
    to.meta.previousPath = from.path;
    next();
});

export default router
